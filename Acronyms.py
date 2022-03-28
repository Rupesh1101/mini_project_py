# This program creates short form of a word.

user_input = input('Enter a phrase:')

text = user_input.split()

a = " "

for i in text:
    a = a + str(i[0].upper())

print(a)

'''
Input - Hyper Text Transfer Protocol

Output - HTTP
'''