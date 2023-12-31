#define the function
def demofunction():
    print('this is demo function')


#call the function
demofunction()

#function with arguments
def add(x,y):
    sum=x+y
    print(sum)

x=int(input('enter the number'))
y=int(input('enter the number'))
add(x,y)


#function with arguments
def check(num):
    if num %2==0:
        return 'even no'
    else:
        return 'odd no'

result=check(15)
print(result)


# sum of even numbers from the  list
def sumofevenno(arr):
    sum=0
    for a in arr:
        if a %2 == 0:
            sum+=a
    return sum

x=[10,11,12,13,14,15,16]
result=sumofevenno(x)
print(result)


# mambership  operator
list1=['a','b','c','d']
print('a' in list1)
print('z' not in list1)
print('b' not in list1)


def checkvowel(arr):
    count=0
    vow=['a','e','i','o','u','A','E','I','O','U']
    for a in arr:
        if(a  in vow):
            count+=1
    return count



q='what is your name'
result=checkvowel(q) 

print(f'the no of vowels are {result}')

def sumofno(arr):
    sume=0
    sumo=0
    for a in arr:
        if a %2 == 0:
            sume+=a
        else:
            sumo+=a
    return sume,sumo

x=[10,11,12,13,14,15,16]
result=list(sumofno(x))
print(f'sum of even no is {result[0]} \nsum of odd no is {result[1]}')

