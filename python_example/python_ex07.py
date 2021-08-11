import time
import random

print(time.localtime(time.time()))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

print(random.random())
print(random.uniform(1, 10))

print(random.randint(1, 10))
print(random.randint(1, 100))