# MNIST 분류 보델 사용하기
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

# MNIST 데이터셋 가져오기 - 데이터셋을 가져와 정규화하는 부분, 이미 학습된 모델을 불러와 사용하기 때문에 테스트셋만 사용
_, (x_test, y_test) = mnist.load_data()
x_test = x_test / 255.0 # 데이터 정규화

# 모델 불러오기 - load_model()를 이용해 모들 불러옴
# summary() 함수로 저장된 모델 정보를 확인
# 테스트셋 데이터를 이용해 모델 성능을 평가 
model = load_model('mnist_model.h5')
model.summary()
model.evaluate(x_test, y_test, verbose=2)

# 테스트셋에서 20번째 이미지 출력
# imshow() 함수를 이용해 테스트셋의 20번째 숫자를 출력
# 실제 예측된 값과 비교하기 위해 이미지로 출력해 봄
plt.imshow(x_test[20], cmap="gray")
plt.show()

# 테스트셋에서 20번째 이미지 클래스 분류
# predict_classes() 함수는 입력 데이터에 대한 클래스를 예측(분류)한 값을 반환
# 20번째 숫자 이미지가 어떤 클래스에 포함되어 있는지 판단
picks = [20]
predict = model.predict_classes(x_test[picks])
print("손글씨 이미지 예측값 : ", predict)