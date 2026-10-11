"""
Given the following strings:
'Bring it On'
' Flanked by spaces on either side '
'C:\\Users\\Kanetkar\\Documents'

Write a program to produce the following output using appropriate string functions.
BRING IT ON
bring it on
Bring it on
Bring It On
bRING iT oN
6            # Find first occurance of 'I'
9            # Find first occurance of 'On' 
Bring Him On
Flanked by spaces on either side
 Flanked by spaces on either side
['C:', 'Users', 'Dharmesh', 'Documents']
('C:', '\\', 'Users\\Dharmesh\\Documents')
"""

s1 = 'Bring It On'
s2 = ' Flanked by spaces on either side '
s3 = 'C:\\Users\\Dharmesh\\Documents'
print(s1.upper())
print(s2.lower())
print(s1.capitalize())
print(s1.title())
print(s1.swapcase())
print(s1.find('I'))
print(s1.find('On'))
print(s1.replace('It', 'Him'))
print(s2.strip())
print(s2.rstrip())
print(s3.split('\\'))
print(s3.partition('\\'))