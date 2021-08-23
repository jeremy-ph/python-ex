import pymysql

db = None

try:
    # DB 호스트 정보
    db = pymysql.connect(
        host='172.17.0.3',
        user='root',
        passwd='1234',
        db='chatbot',
        charset='utf8'
    )

    # 데이터 삭제 sql
    id = 1  # 데이터 id(Primary key)
    sql = '''
        DELETE from tb_student where id=%d
    ''' % id

    # 데이터 삭제
    # cursor 객체의 execute()함수로 sql 구문을 실행
    with db.cursor() as cursor:
        cursor.execute(sql)
    db.commit()

except Exception as e:
    print('DB error : ', e)

finally:
    if db is not None:
        print('데이터가 삭제되었습니다.')
        db.close();