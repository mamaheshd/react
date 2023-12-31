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
