import matplotlib.pyplot as plt

# # 직선그래프 예제
# # x, y 축 데이터 정의
# x = [a for a in range(0, 11)]
# y = list(range(0, 11))

# # x, y축 데이터 출력
# print('x축', x)
# print('y축', y)

# # 그래프 출력
# plt.plot(x, y)
# plt.show()


# # 2차 함수 그래프
# # f(x) = x^2
# f = lambda x: x ** 2

# # x, y축 데이터 정의
# x = [x for x in range(-10, 10)]
# y = [f(y) for y in range(-10, 10)]

# # x, y축 데이터 출력
# print('x축', x)
# print('y축', y)

# # 그래프 출력
# plt.plot(x, y)
# plt.show()


# 계정별 온도 바차트
# 데이터 정의
temperatures = [3.3, 34.5, 14.2, -10]
x = list(range(4))
x_labels = ['Spring', 'Summer', 'Fall', 'Winter']

# 바차트 출력
plt.title("Bar Chart")  # 바차트 제목
plt.bar(x, temperatures)    # x, y의 데이터에 따라 바차트를 그린다. x축은 y축 데이터의 카테고리이기 때문에 단순히 인덱스 값의 의미만 가진다.
# x는 range함수를 이용해 0~3까지 요소를 갖는 리스트를 x축 데이터로 사용, y축 데이터는 계절별 온도값을 의미
plt.xticks(x, x_labels) # x축 데이터 위치에 지정된 텍스트 표시
plt.yticks(sorted(temperatures))    # 오름차순으로 정렬된 값을 y축 데이터 위치에 표시
plt.xlabel("season")    # x축 레이블 지정
plt.ylabel("temperature")   # y축 레이블 지정
plt.show()
