number=int(input('Enter the number:'))
msg='even' if number%2==0 else 'odd'
print(msg)

# recursive function
def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)
    
n=int(input('enter a no to calculate factorial'))
f=fact(n)
print(f)

#enumerate: it is a useful function to use with for loop
index_count=0
for latter in 'hello':
    print('At index {index_count} the latter is {latter}')
    index_count+=1

index_count=0
for latter in 'hello':
    print('At index {} the latter is {}'.format(index_count,latter))
    index_count+=1

# use enumerate in above example
for i,latter in enumerate('Welcome'):
    print('At index {} the latter is {}'.format(i,latter))

