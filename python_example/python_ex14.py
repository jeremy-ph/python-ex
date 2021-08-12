import pandas as pd

# 팬더스 버전 체크
print(pd.__version__)

# sample.xlsx 엑셀파일 읽어오기, error시 engine='openpyxl' 추가
user_list = pd.read_excel('../sample.xlsx', sheet_name='Sheet1', engine='openpyxl')
print(user_list)