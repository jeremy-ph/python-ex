from numpy.lib.function_base import sort_complex
import pandas as pd

# 인덱스를 생략한 시리즈 객체
numbers = pd.Series([100,200,300])

# 시리즈 객체 출력
print(numbers)

# 인덱스를 지정한 시리즈 객체
scores = pd.Series([90,80,99], index=['Kor', 'Math', 'Eng'])

# 시리즈 객체 출력
print(scores)

# 시리즈 랙체의 인덱스 출력
print(scores.index)

# 시리즈 객체의 데이터 출력
print(scores.values)

# 원하는 위치의 인덱스, 데이터값 출력
print(scores.index[1], scores.values[1])