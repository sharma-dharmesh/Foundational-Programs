"""For the following strings find out which are having only alphabets, which are numeric, which are alphanumeric, which are lowercase, which are uppercase. Also find out whether 'And Quite Flows The Don' begins with 'And' or ends with 'And':
'NitiAayog'
'And Quiet Flows The Don'
'1234567890'
'Make $1000 a day'
"""
s1 = 'NitiAayog'
s2 = 'And Quiet Flows The Don'
s3 = '1234567890'
s4 = 'Make $1000 a day'
print(f's1 = {s1}')
print(f's2 = {s2}')
print(f's3 = {s3}')
print(f's4 = {s4}')

print('\nCheck isalpha')
print(s1.isalpha())
print(s2.isalpha())
print(s3.isalpha())
print(s4.isalpha())

print('\ncheck isdigit')
print(s1.isdigit())
print(s2.isdigit())
print(s3.isdigit())
print(s4.isdigit())

print('\ncheck isalphnum')
print(s1.isalnum())
print(s2.isalnum())
print(s3.isalnum())
print(s4.isalnum())

print('\ncheck islower')
print(s1.islower())
print(s2.islower())
print(s3.islower())
print(s4.islower())

print('\ncheck isupper')
print(s1.isupper())
print(s2.isupper())
print(s3.isupper())
print(s4.isupper())

print('\ncheck startswith and endswith on s2')
print(s2.startswith('And'))
print(s2.endswith('And'))