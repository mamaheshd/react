# lambda expression allow us to create anonymous function. This basically means we can quickly make ad-hoc function without nedding to properly defined the function using keyword def.
# def square(num):return(num**2)
square=lambda num:num**2

result=square(5)
print(result)

#filter
numbers=[2,3,4,5,6,12,8,10,11,9]
result=list(filter(lambda num : num%2==0,numbers))
print(result)