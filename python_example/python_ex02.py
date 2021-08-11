# 조건문
# money = 5000
# if money > 2000:
#     print("택시")
# else:
#     print("걸어")

# pocket = ['paper', 'cellphone']
# card = True
# if 'momey' in pocket:
#     # print("taxi")
#     pass
# elif card:
#     print("taxi")
# else:
#     print("bus")

score = 70
if score >= 60:
    message = "success"
else: 
    message = "failure"
# print(message)

# 3항 연산자 ?
message = "success" if score >=60 else "failure"
# print(message)

# treeHit = 0
# while treeHit < 10:
#     # treeHit = treeHit + 1
#     treeHit += 1
#     print("나무를 %d번 찍음." %treeHit)
#     if treeHit == 10:
#         print("넘어감")

# test_list = ['one', 'two', 'three']
# for i in test_list:
#     print(i)

# a = [(1,2),(3,4),(5,6)]
# for (first,last) in a:
#     print(first,last)
#     print(first+last)

marks = [90,25,67,54,80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)