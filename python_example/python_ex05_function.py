
# def is_even(number):
#     return number % 2 == 0

# numbers = range(1, 21)
# even_list = list(filter(is_even, numbers))
# print(even_list)


# def call_10_times(func):
#     for i in range(5):
#         #callback
#         func(i)

# def print_hello(number):
#     print("Hi~ Hello : ", number)

# call_10_times(print_hello)


# # lambda
# def call_10_times(func):
#     for i in range(5):
#         #callback
#         func(i)

# call_10_times(lambda number: print("Hi~ Hello : ", number))



# def only2(number):
#     return number % 2 == 0

# a = list(range(10))
# # print(a)

# # filter
# b = filter(only2, a)
# # print(list(b))

# for i in b:
#     print(i)



# a = list(range(10))
# # filter
# b = filter(lambda number: number % 2 == 0, a)
# # print(list(b))
# for i in b:
#     print(i)


# only2 = lambda number: number % 2 == 0
# a = list(range(10))
# b = filter(only2, a)
# print(list(b))


# # map
# def axa(number):
#     return number * number

# a = list(range(10))
# print(list(map(axa, a)))


# map
# a = list(range(10))
# # print(list(map(lambda number: number * number, a)))

# # list comprehension(리스트 내포) filter + map
# print([i * i for i in a if i % 2 == 0])