#list compression allows us to build  out the list using a different notation. You can think of it as essentially a one line for loop build inside [] brackets.
# using for loop to calculate square of a no.
for x in range(1,11):
    print(x**2)

#converting above program using listcompression 
    
numbers=[x**2 for x in range(1,11)]
print(numbers)

number=[x for x in range(1,11) if x%2==0]
print(number)

cel=[10,20,30,40,50,60,70,80,90,100]
f=[(9/5)*c+32 for c in cel]
print(f)