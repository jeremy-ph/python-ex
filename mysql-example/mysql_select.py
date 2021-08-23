import pymysql
import pandas as pd

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

    # # 초기 데이터 DB에 추가
    # student = [
    #     {'name': 'Park', 'age': 35, 'address': 'PUSAN'},
    #     {'name': 'Jeremy', 'age': 44, 'address': 'SEOUL'},
    #     {'name': 'Lee', 'age': 33, 'address': 'HANAM'},
    #     {'name': 'Hong', 'age': 29, 'address': 'GWANGJU'},
    #     {'name': 'Kim', 'age': 41, 'address': 'SEOUL'},
    #     {'name': 'Nam', 'age': 25, 'address': 'ILSAN'},
    # ]
    # for i in  student:
    #     with db.cursor() as cursor:
    #         sql = '''
    #             INSERT tb_student(name, age, address) values('%s', %d, '%s')
    #         ''' % (i['name'], i['age'], i['address'])
    #         cursor.execute(sql)
    # db.commit() # 커밋


    # 30대 학생만 조회
    cond_age=30
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = '''
            select * from tb_student where age > %d
        ''' % cond_age
        cursor.execute(sql)
        results = cursor.fetchall()
    print(results)

    # 이름 검색
    cond_name = 'Jeremy'
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = '''
            select * from tb_student where name = '%s'
        ''' % cond_name
        cursor.execute(sql)
        resurt = cursor.fetchone()
    print(resurt['name'], resurt['age'])

    # pandas 데이터프레임으로 표현
    df = pd.DataFrame(results)
    print(df)

except Exception as e:
    print('DB error : ', e)

finally:
    if db is not None:
        print('데이터 검색 완료.')
        db.close();