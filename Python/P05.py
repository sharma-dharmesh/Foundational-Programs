"""Write a program to swap two variables without using the third variable"""

a = 20
b = 30

print(f'Before Swapping a = {a} and b = {b}')
a = a + b
b = a - b
a = a - b
print(f'After Swapping a = {a} and b = {b}')