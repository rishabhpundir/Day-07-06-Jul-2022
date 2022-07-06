# to check if the first character is a digit

# num = '833434'
# # print(num[0].isdigit())
# numbers = '0123456789'
# if num[0] in numbers:
#     print(True)

# -------------------------------------------------------------------

# to find a string or set of strings
# import re

# string = 'This is a test the string for the implementing RegEx the module of the Python Pragramming Language.'

# # x = re.search('Python', string)
# # x = re.findall('in', string)
# # x = re.split('\s', string)
# # x = re.sub('the', '"the replaced with 9"', string)
# print(x)

# -------------------------------------------------------------------

# Pallindrome

# def checker(string):
#     x = string[::-1]
#     if x == string:
#         print(f'"{string}" is a pallindrome.')
#     else:
#         print(f'"{string}" is not a pallindrome.')

# text = str(input('Enter a string to check : '))
# checker(text)

# -------------------------------------------------------------------

# Factorial program

# def factorial(num):
#     x=1
#     if num > 0:
#         for i in range(0, num):
#             if i != num:
#                 x = x*(num-i)
#         print(f'Factorial of {num} is {x}.')
#     else:
#         print(f'Factorial of 0 is 1.')

# number = int(input('Enter a number to produce factorial of : '))
# factorial(number)

# OR

# def factorial(num):
#     if num == 1:
#         return num
#     else:

#         return num * factorial(num-1)

# print(factorial(4))

# -------------------------------------------------------------------

# Fibonacci Series

# def fibonacci(num):
#     loop_runs = True
#     a = 0
#     b = 1
#     c = 0
#     print(f'{a}\n{b}')
#     while num-1:
#         c = a + b
#         a = b
#         b = c
#         print(f"{c} ")
#         num = num-1

# f_range = int(input('Enter a range for fibonacci series : '))
# fibonacci(f_range)

# -------------------------------------------------------------------

# # a * pyramid

# stars = [' ', ' ', ' ', ' ', ' ']
# for i in range(0, len(stars)):
#     stars[len(stars)-1-i] = '* '
#     print(''.join(stars))

# -------------------------------------------------------------------

# # a left half * pyramid

# stars = [' ', ' ', ' ', ' ', ' ']
# for i in range(0, len(stars)):
#     stars[len(stars)-1-i] = '*'
#     print(''.join(stars))

# -------------------------------------------------------------------

# # a right half * pyramid

# stars = [' ', ' ', ' ', ' ', ' ']
# for i in range(0, len(stars)):
#     stars[i] = '*'
#     print(''.join(stars))

# -------------------------------------------------------------------

# Prime number checker

# def prime_checker(num):
#     x = False
#     for i in range(2, num):
#         if num % i == 0:
#             x = True
#             break

#     if num==0 or num==1 or x==True:
#         print(f'{num} is not a prime number.')
#     else:
#         print(f'{num} is a prime number.')
    

# number = int(input('Enter a number to check its prime number status : '))
# prime_checker(number)
