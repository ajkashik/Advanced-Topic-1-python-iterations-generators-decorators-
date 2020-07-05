# method 1

def decorators(arg):
    def inner(*args,**kwargs):
        print("Let's go!")
        arg(*args,**kwargs)
    return inner

@decorators
def number(a):
    print(f"Number is {a}")
    
number(7)
        
#method 1

def decorators2(arg2):
    def inner2(*args,**kwargs):
        print("I am here")
        arg2(*args,**kwargs)
    return inner2

@decorators2
def add(a,b):
    return a+b

print(add(2,3))

