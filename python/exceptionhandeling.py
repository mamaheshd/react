# try test block of code for error
# except let you handel the error
# else lets you execute when there is no error
#finally lets you execute code, regardless of the result of the try except

try:
    print('hello')
except:
    print('Error')


try:
    print(hello)
except:
    print('Error occured')
# many exception
try:
    print(hello)
except NameError:
    print('variable is not defined') 
except:
    print('exception occurs') 

finally:
    print('code execution completed')

try:
    print(20)
except:
    print('Error occured')
    
else:
    print('no error')

# #raise exception
# a=50
# if a>40:
#     raise Exception('no is greater then 40 is not allowed')

# a='lol'
# if not type(a) is int:
#     raise TypeError('only integer is allowed')