"""Demonstrate how to create simple and multi-line strings and whether a string can change after creation. Also show the usage of build-in functions len(), min() and max() on a string."""

msg = 'Hello'
print(msg)

msg2 = 'He said, \'Let Us Python\'.'
file1 = 'C\\temp\\newfile'
file2 = r'C:\\temp\newfile'
print(msg2)
print(file1)
print(file2)

msg3 = 'What is this life if full of care...\
    We have no time to stand and stare'
msg4 = """What is this life if full of care...
We have no time to stand and stare"""
msg5 = ('What is this life if full of care...'
        'We have no time to stand and stare')
print(msg3)
print(msg4)
print(msg5)

msg6 = 'MacLearn!!'
print(msg6 * 3)

msg7 = 'Utopia'
msg8 = 'Today!!!'
msg7 = msg7 + msg8
print(msg7)

print(len('Hoopla'))
print(min('Hoopla'))
print(max('Hoopla'))
