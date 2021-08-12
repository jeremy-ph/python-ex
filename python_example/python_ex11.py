import numpy as np

# arr = np.array([1,2,3])
# print(arr)
# print(type(arr))


# matrix = np.array([ [1,2,3],[4,5,6] ])
# print(matrix)


# A = np.array([ [1,2], [3,4]])
# B = np.array([ [1,1], [1,1]])
# C = A + B   # 행렬 덧셈 연산
# print(C)


# A = np.array([ [1,2], [3,4], [5,6] ])
# B = np.array([ [2,3], [2,3] ])
# C = np.matmul(A, B) # 행렬 곱셈 A * B
# print(C)    # 결과는 3x2 행렬


A = np.array([ [1,2], [3,4] ])  # 2X2 행렬
k = 10  # 스칼라 Scalar(상수)
C = k * A   # 스칼라곱
print(C)    # 결과 2X2 행렬 

