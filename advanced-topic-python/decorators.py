#first method

def func1():
    print("I am function 1")
    
def func2():
    print("I am function 2")
    
    
def out(agr):
    def inner():
        print("I am inner function")
        agr()
    return inner

poo=out(func1)
poo()

print(" ")

#second method

@decorators
def animal():
    print("Tiger")

@decorators
def fish():
    print("Hilsha")


def decorators(argument):
    def inner_function():
        print("Fish or Animal")
        argument()
    return inner_function


animal()
fish()