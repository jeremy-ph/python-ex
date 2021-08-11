import sys # sys 모듈 불러오기

# print(sys.argv) # 시스템 인자로 들어온 리스트 내용 출력
# msg = sys.argv[1]   # 'hello'   
# cnt = int(sys.argv[2])  # 10

# for i in range(cnt):
#     print(i, msg)

for n in range(100):
    print(n)
    if n == 10:
        sys.exit()
