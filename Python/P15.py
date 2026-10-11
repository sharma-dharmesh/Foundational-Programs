"""
Find all occurrences of 'T' in the string 'The Terrible Tiger Tore The Towel'. Replace all occurrences of 'T' with 't'.
"""

s = 'The Terrible Tiger Tore The Towel'
pos = s.find('T', 0)
print(pos, s[pos])
while pos != -1:
    pos = s.find('T', pos + 1)
    if pos == -1:
        print("That's all!")
        break
    print(pos, s[pos])

c = s.count('T')
s = s.replace('T', 't', c)
print(s)
