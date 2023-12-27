# loop for and while loop

numbers=[10,20,30,40,50]
for num in numbers:
    print(num,end=' ')

print('\n')

text='Helo words'
for letter in text:
    print(letter,end=' ')
print('\n')
for i in range(1,11):
    print(i,end=" ")
print('\n')
for j in range(1,21):
    if(j%2==0):
        print(j,end=' ')
print('\n')
#break
fruits=['apple','mango','orange','papaya','charry']
for f in fruits:
    if f=='orange':
        break
    print(f)
print('\n')    
fruits=['apple','mango','orange','papaya','charry']
for f in fruits:
    if f=='orange':
        continue
    print(f)
# while loop
x=1
while(x<=10):
    print(x,end=' ')
    x+=1

