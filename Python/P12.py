"""For a given string 'Bamboozled', write a program to obtain the following output:
B a #from positive index
B a #from negative index
e d #from positive index
e d #from negative index
mboozled
mboozled
mboozled
Bamboo
Bamboo
Bamboo
Bamboo
delzoobmaB
Bamboozled
Bmoze
Bbzd
Boe
BamboozledHype!
BambooMonger!
"""

s = 'Bamboozled'

# extract B a
print(s[0], s[1])
print(s[-10], s[-9])

# extract e d
print(s[8], s[9])
print(s[-2], s[-1])

# extract mboozled
print(s[2:10])
print(s[-8:])
print(s[2:])

# extract Bamboo
print(s[0:6])
print(s[:6])
print(s[-10:-4])
print(s[:-4])

# reverse Bamboozled
print(s[::-1])

# extract Bamboozled
print(s[::])

# extract Bmoze
print(s[::2])

# extract Bbzd
print(s[::3])

# extract Boe
print(s[::4])

# print BamboozledHype!
print(s + 'Hype!')

# print(BambooMonger!)
print(s[:6] + 'Monger!')