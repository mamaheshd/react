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
