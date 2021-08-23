import pymysql
# pip install pymysql

db = None

try:
    # DB 호스트 정보에 맞게 입력해주세요
    db = pymysql.connect(
        host='172.17.0.3',
        user='root',
        passwd='1234',
        db='chatbot',
        charset='utf8'
    )

except Exception as e:
    print(e)    # DB 연결 실패 시 오류 내용 출력

finally:
    if db is not None:  # DB가 연결된 경우에만 접속 시도
        db.close()
        print("DB 연결 닫기 성공")