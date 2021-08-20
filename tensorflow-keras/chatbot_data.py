# 문장 감정 분류 CNN 모델 
import pandas as pd
import tensorflow as tf
from tensorflow.keras import preprocessing
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Dense, Dropout, Conv1D, GlobalMaxPool1D, concatenate

# 데이터 읽어오기 1
# CNN 모델 학습시 필요한 Q(질문)와 label(감정) 데이터를 features와 labels리스트에 저장
train_file = "./ChatbotData.csv"
data = pd.read_csv(train_file, delimiter=',')
features = data['Q'].tolist()
labels = data['label'].tolist()

# 단어 인덱스 시퀀스 벡터 2
# 불러온 질문 리스트(features)에서 문장을 하나씩 꺼내와 text_to_word_sequence()함수를 이용해 단어 스퀀스(단어 토큰의 순차절 리스트)를 만든다
# 예) "3박4일 놀러가고 싶다 => ['3박4일', '놀러가고', '싶다']" 이렇게 생성된 단어 스퀀스를 말뭉치(corpus) 리스트에 저장
# 텐스플로 토크나이저의 texts_to_sequences()함수를 이용해 단어 내 모든 잔어를 시퀀스 번호로 변환
corpus = [preprocessing.text.text_to_word_sequence(text) for text in features]
tokenizer = preprocessing.text.Tokenizer()
sequence = tokenizer.texts_to_sequences(corpus)
word_index = tokenizer.word_index

# 문장의 길이가 다르기에 벡터크기가 달라진다. CNN 모델의 입력계층은 고정된 갯수의 입력 노드를 가지고 있다
# 그래서 MAX_SEQ_LEN 크기만큼 넉넉히 넓힌다. MAX_SEQ_LEN 보다 작아 남는 공간은 0으로 채우는 작업을 한다
# 이런 과정을 패딩(padding)처리라 한다. 케라스에서는 pad_sequences()함수를 통해 시퀀스의 패딩 처리를 쉽게 할 수 있다
# maxlen 인자로 시퀀스의 최대 길이를 정하는데, 학습시킬 문장 데이터들을 사전에 분석해 최대 몇 개의 단어 토큰으로 구성되어 있는지 파악해야 함
# 너무 크면 자원이 낭비, 너무 작으면 데이터 손실이 생긴다
MAX_SEQ_LEN = 15 # 단어 시퀀스 벡터 크기
padded_seqs = preprocessing.sequence.pad_sequences(sequence, maxlen=MAX_SEQ_LEN, padding='post')

# 학습용, 검증용, 테스트용 데이터셋 생성 3
# 학습셋:검증셋:테스트셋 = 7:2:1
# 패딩 처리된 시퀀스(padded_seqs) 백터 리스트와 감정(labels) 리스트 전체를 데이터 셋 객체로 만듬
# 데이터를 랜덤으로 섞은 후 학습용, 검증용, 테스트용 데이터셋을 7:2:1 비율로 나눠 실제 학습에 필요한 데이터셋 객체를 각각 분리
ds = tf.data.Dataset.from_tensor_slices((padded_seqs, labels))
ds = ds.shuffle(len(features))

train_size = int(len(padded_seqs) * 0.7)
val_size = int(len(padded_seqs) * 0.2)
test_size = int(len(padded_seqs) * 0.1)

train_ds = ds.take(train_size).batch(20)
val_ds = ds.skip(train_size).take(val_size).batch(20)
test_ds = ds.skip(train_size + val_size).take(test_size).batch(20)

# 하이퍼파라미터 설정
dropout_prob = 0.5
EMB_SIZE = 128
EPOCH = 5
VOCAB_SIZE = len(word_index) + 1 # 전체 단어 수 

# CNN 모델 정의 4
# CNN 모델을 케라스 함수형 모델(functional model)방식으로 구현
# 입력 계층은 케라스의 Input() 으로 생성, shape 인자로 입력 노드에 들어올 데이터를 형상(shape)을 지정함
# 실제 패딩 처리된 시퀀스 백터의 크기(MAX_SEQ_LEN)로 설정
# 앞서 단어별로 패딩 처리된 시퀀스 백터는 희소 백터를 입력받아 밀집 벡터로 변환해 준다
# 단어의 갯수(VOCAB_SIZE)와 임베딩 결과로 나올 밀집 켁터의 크기(EMB_SIZE), 입력되는 시퀀스 벡터의 크기(MAX_SEQ_LEN)를 Embedding()의 인자로 사용해 임베딩 계층을 생성
# 단어 임베딩 부분의 마지막에는 50% 확률로 Dropout()을 생성함, 학습과정에 발행할지 모를 오버피팅(과적합)에 대비
input_layer = Input(shape=(MAX_SEQ_LEN,))
embedding_layer = Embedding(VOCAB_SIZE, EMB_SIZE, input_length=MAX_SEQ_LEN)(input_layer)
dropout_emb = Dropout(rate=dropout_prob)(embedding_layer)

# 임베딩 벡터에서 특징 추출을 하는 영역
# Conv1D()를 이용해 크기가 3, 4, 5인 합성곱 필터를 128개씩 사용한 합성곱 계층을 3개 생성
# 합성곱 연산 과정 - 필터 크기에 맞게 입력 데이터 위를 슬라이딩하게 되는데, 이는 3,4,5-gram 언어 모델의 개념과 비슷
# 임베딩 벡터를 합성곱 계층의 입력으로 받아 GlobalMaxPool1D()를 이용해 최대 풀링 연산을 수행함
# 완전 연결 계층에 전달될 수 있도록 concatenate()를 이용해 각각 병렬로 처리된 합성곱 계층의 특징맵 결과를 하나로 묶어줌
conv1 = Conv1D(
    filters=128,
    kernel_size=3,
    padding='valid',
    activation=tf.nn.relu)(dropout_emb)
pool1 = GlobalMaxPool1D()(conv1)

conv2 = Conv1D(
    filters=128,
    kernel_size=4,
    padding='valid',
    activation=tf.nn.relu)(dropout_emb)
pool2 = GlobalMaxPool1D()(conv2)

conv3 = Conv1D(
    filters=128,
    kernel_size=5,
    padding='valid',
    activation=tf.nn.relu)(dropout_emb)
pool3 = GlobalMaxPool1D()(conv3)

# 3, 4, 5-gram 이후 합치기
concat = concatenate([pool1, pool2, pool3])

# CNN 모델의 마지막 단계인 완전 연결 계층 구현. 기본적인 심층 신경망을 사용하기 때문에 코드가 간단함
# Dense()를 이용해서 128개의 출력 노드를 가지고, relu 활성화 함수를 사용하는 Dense 계층을 생성
# 합성곱 연산과 맥스 풀링으로 나온 3개의 특징맵 데이터를 입력으로 받는다
# 챗봇 데이터 문장에서 3가지 클래스로 감정 분류해야 하기 때문에 출력 노드가 3개인 Dense()를 생성
# 결과로 나온 값(logits)을 점소score라 부름. 출력 노드에서 3개의 점수가 출력. 가장 큰 점수를 가진 노드 위치가 CNN모델이 예측한 결과Class가 된다
# logits에서 나온 점수를 소프트맥스 계층을 통해 감정 클래스별 확률을 계산
# 클래스 분류 모델classification problem을 학습할 때 주로 손실값loss을 계산하는 함수로 sparse_categorical_crossentropy를 사용
hidden = Dense(128, activation=tf.nn.relu)(concat)
dropout_hidden = Dropout(rate=dropout_prob)(hidden)
logits = Dense(3, name='logits')(dropout_hidden)
predictions = Dense(3, activation=tf.nn.softmax)(logits)

# 모델 생성 5
# 케라스 모델을 생성할 때 Model()을 사용하는데, 인자로는 앞서 생성한 입력 계층(input_layer)과 출력 계층(predictions)을 사용함
# 모델 정의 후 실제 모델을 mnodel.compile() 함수를 통해 CNN 모델을 컴파일함.
# 최적화 방법에는 adam을, 손실 함수에는 sparse_categorical_crossentropy를 사용
# 정확도를 확인하기 위해 metrics에 accuracy를 사용. 손실값만 확인할때는 생략해도 된다
model = Model(inputs=input_layer, outputs=predictions)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 모델 학습 6
# 첫 번째 인자에는 학습용 데이터셋, 두번째 validation_date인자에는 검증용 데이터 셋, 에포크값을 5로 설정했므로 5회 반복함
# verbose인자가 1인 경우에는 모델 학습 시 진행과정을 상세히 보여줌. 학습 과정을 생략하고 싶으면 0으로 설정하면 됨
model.fit(train_ds, validation_data=val_ds, epochs=EPOCH, verbose=1)

# 모델 평가(테스트 데이터셋 이용) 7
# evaluate() 함수를 이용해 성능평가. 인자로 테스트용 데이터셋을 사용
loss, accuracy = model.evaluate(test_ds, verbose=1)
print('Accuracy: %f' % (accuracy * 100))
print('loss: %f' % (loss))

# 모델 저장 8
# 학습이 완료된 모델을 h5 파일 포맷으로 저장.
model.save('cnn_model.h5')