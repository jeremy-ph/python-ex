pin = "880111-1066257"
yyyymmdd = "19880111"
num = 123456789
# print(yyyymmdd[7:8])

a = "a:b:c:d"
b = a.replace(":","#")
# print(b)

a = [3, 2, 5, 4, 1]
a.sort()
a.reverse()
# print(a)

a = ['Life', 'is', 'too', 'short']
result = ' '.join(a)
# print(result)

b = [3, 2, 5, 4, 1]
a = (1, 2, 3)
a = a + (4,)
# print(type(b))
# print(type(a))
# print(len(a))
# print(a)

t1 = (1, 2, 'a', 'b', 5)
t2 = 3, 4, 7
# print(t1 + t2)

dic = {'name':'hong', 'age':15 }
# print(dic['name'])

dic['school'] = 'seoul'
# print(dic)

# del dic['age']
# print(dic)

# print(dic.keys())
# print(dic.values())
# print(dic.items())

# for i, v in dic.items(): 
#     print("키는: " + str(i))
#     print("벨류는: " + str(v))

# dic.clear()
# print(dic)    

# print(dic.get('age', '없음'))
# print('name' in dic)


l = [1,2,2,3,4,4,5]
# print(l)
# print(set(l))
# print(list(set(l)))

ss1 = set("hello")
# print(ss1)

# s1 = {1,2,3}
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

# print(s1 & s2)
# print(s1.intersection(s2))

# print(s1 | s2)
# print(s1.union(s2))

# print(s1 - s2)
# print(s2 - s1)

# s1.add(7)
# s1.remove(1)
s1.update([7,8,9])
# print(s1)

a = 1
# if a:
#     print(a)

# a = [1,2,3,4]
# while a:
#     print(a)
#     a.pop()

a = [1,2,3,4]
b = a[:]

a[1] = 4
# print(id(a))
# print(id(b))
# print(a is (b))    



from copy import copy
a = [1,2,3]
b = copy(a)
# print(a)
# print(b)
# print(id(a))
# print(id(b))


# a, b = ('python', 'life')
[a,b] = ['python', 'life']
# a = b = 'hello' 
# print(a)
# print(b)

a = 3
b = 5
a,b = b,a
print(a)
print(b)