text='Python is a high level programming language' 
print(text)

# count no of characters in a strings
print(len(text))

# indexing
print(text[0])
print(text[-1]) #print from back sides

# slicing
print(text[2:10]) #2 to 9
print(text[:20]) # 0 to 19
print(text[:]) # all
print(text[10:])
#negative slicing
print(text[-15:-1])

#built in string methods
# .upper()
# .lower()
# .split()-> split the word from space by default

print(text.upper())
print(text.lower())
print(text.split())
print(text.split('level'))

#string formatting with placeholder
print('we are learing %s'%'python')
print('we are learing %s at %s'%('python','Dursikshya'))





