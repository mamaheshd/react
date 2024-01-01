# *args when function parameter starts with ana asterisk, it allows for an arbitary number of arguments and function takes them in as a tuple of values.

def demoFunction(*args):
    return sum(args)
    
result=demoFunction(10,20,30,40)
print(result)

#**kwargs it builds a dictionary of key value pair
def demo(**kwargs):
    if 'fruit' in kwargs:
        print(f'my favorite fruit is {kwargs["fruit"]}')
    else:
        print('not a favroite fruit')

demo(fruit='apple')
