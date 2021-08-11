# def print_user(user, score):
#     print("name : %s" % user.get('name'))
#     print("age : %d" % user.get('age'))
#     print("score : %d" % score)

# user = {'name': 'Kei', 'age': 35 }
# score = 86
# print_user(user, score)


# print('integer: {} / float : {} / string : {}'.format(10, 3.14, "hello"))

# print('integer: {0} / float : {1} / string : {2}'.format(10, 3.14, "hello"))

# print('float: {1} / integer : {0} / string : {2}'.format(10, 3.14, "hello"))

# numbers = [10, 11, 12, 13, 14]
# for idx, value in enumerate(numbers):
#     print('index: {} / value: {}'.format(idx, value))


# print(str(10))
# print(type(str(10)))
# print(str('hello'.upper()))
# print(str('HELLO'.lower()))
# print(type(str([10,20,30])))

# names = ['Kei', 'Tonny', 'Grace', 'Jenny', 'Jaeyoo']
# print(','.join(names))
# print('/'.join(names))
# print(' '.join(names))

# names = ['Kei', 'Tonny', 'Grace', 'Jenny', 'Jaeyoo']
# names_str = ','.join(names)
# print(names_str)
# print('ID: %s' %id(names_str))

# names_split = names_str.split(',')
# print(names_split)
# print('ID: %s' %id(names_split))



# str = "I want to be a great programmer"
# print(str.find('I'))
# print(str.find('want'))
# print(str.find('be'))

# str = " I want to be a great programmer. "
# new_str = str.strip()
# print(new_str)

# f = lambda x: x * 2
# print(f(4))

# numbers = range(1,21)
# even_list = list(filter(lambda n: n%2==0, numbers))
# print(even_list)

# def square(number):
#     return number ** 2

# number = range(1, 5)
# square_list = list(map(square, number))
# print(square_list)

number = range(1, 5)
square_list = list(map(lambda number: number ** 2, number))
print(square_list)