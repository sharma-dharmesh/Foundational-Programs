"""Write a program that generates 5 random numbers in the range 10 to 50. Use a seed value of 6. Make a provision to change this seed value every time you execute the program by associating it with the time of execution"""


import random
# random.seed(6)
# random.seed(8)
random.seed(12)

for i in range(5):
    print(random.randint(10, 50))
