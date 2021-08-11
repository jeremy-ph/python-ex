import pickle
import time

f = open('setting.txt', 'rb')
setting = pickle.load(f)
f.close()
print(setting)
print(time.time())
print(time.localtime(time.time()))
print(time.struct_time(tm_year=2021, tm_mon=1, tm_mday=31, tm_hour=1, tm_min=2, tm_sec=23, tm_wday=4, tm_yday=31,tm_isdst=0))