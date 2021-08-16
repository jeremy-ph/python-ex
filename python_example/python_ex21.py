# Word2Vec 모델 학습 예제
from os import sendfile
from gensim.models import Word2Vec
from konlpy.tag import Komoran
import time

# 네이버 영화 리뷰 데이터 읽어옴
# 'r'은 read , 'w'는 write, '\t' 는 TAB 을 의미, \t를 기준으로 데이터를 분리
# data[1:] 첫 번째 행의 헤더를 제거하고 리뷰 데이터를 만든다
def read_review_data(filename):
    with open(filename, 'r') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:] # 해더 제거
    return data

# 학습 시간 측정 시작
start = time.time()

# 리뷰 파일 읽어 오기
print('1) 말뭉치 데이터 읽기 시작')
review_data = read_review_data('./ratings.txt')
print(len(review_data)) # 리뷰 데이터 전체 갯수
print('1) 말뭉치 데이터 읽기 완료 : ', time.time() - start)

# 문장 단위로 명사만 추출해 학습 입력 데이터로 만듦
print('2) 형태소에서 명사만 추출 시작')
komoran = Komoran()
docs = [komoran.nouns(sentence[1]) for sentence in review_data]
print('2) 형태소에서 명사만 추출 완료 : ', time.time() - start)

# Word2Vec 모델 학습
# sentences : Word2Vec 모델 학습에 필요한 문장 데이터, 모델의 립력값으로 사용
# size : 단어 임베딩 벡터의 차원(크기)
# window : 주변 단어 윈도우의 크기
# hs : 0(0이 아인 경우 음수 샘플링 사용), 1(모델 학습에 softmax 사용)
# min_count : 단어 최소 빈도 수 제한(설정된 min_count 빈도 수 이하의 단어들은 학습하지 않음)
# sg : 0(CBOW 모델), 1(skip-gram 모델)
print('3) Word2Vec 모델 학습 시작')
model = Word2Vec(sentences=docs, vector_size=200, window=4, hs=1, min_count=2, sg=1)
print('3) Word2Vec 모델 학습 완료 : ', time.time() - start)

# 모델 저장
print('3) 학습된 모델 저장 시작')
model.save('nvmc.model')
print('3) 학습된 모델 저장 완료 : ', time.time() - start)

# 학습된 말뭉치 수, 코퍼스 내 전체 단어 수
print("corpus_count : ", model.corpus_count)
print("corpus_total_words : ", model.corpus_total_words)

############## 결과 출력 ##############
# 1) 말뭉치 데이터 읽기 시작
# 200000
# 1) 말뭉치 데이터 읽기 완료 :  0.39179110527038574
# 2) 형태소에서 명사만 추출 시작
# 2) 형태소에서 명사만 추출 완료 :  118.13883066177368
# 3) Word2Vec 모델 학습 시작
# 3) Word2Vec 모델 학습 완료 :  146.57095432281494
# 3) 학습된 모델 저장 시작
# 3) 학습된 모델 저장 완료 :  147.6633312702179
# corpus_count :  200000
# corpus_total_words :  1076896