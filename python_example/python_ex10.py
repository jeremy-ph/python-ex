# try:
#     a = 10
#     b = 0 
#     c = a / b
#     print(c)
# except Exception as e:
#     print(e)

# try:
#     a = 10
#     b = 'zero' 
#     c = a / b
#     print(c)
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)

import pickle

f = open('setting.txt', 'wb')
try:
    setting = [{'title': 'python program'}, {'author': 'Kei'}]
    pickle.dump(setting, f)
except Exception as e:
    print(e)
finally:
    f.close()