"""
Write a program that generates the following output from the string 'Shenanigan'
S h
a n
enanigan
Shenan
Shenan
Shenan
Shenan
Shenanigan
Seaia
Snin
Saa
ShenaniganType
ShenanWabbite
"""

s = 'Shenanigan'
print(s[:3])
print(s[4:6])
print(s[3:])
print(s[0:7])
print(s[:7])
print(s[-10:-4])
print(s[-5::-1])
print(s[::])
print(s[::2])
print(s[::3])
print(s[::4])
print(s + 'Type')
print(s[:6] + 'Wabbite')