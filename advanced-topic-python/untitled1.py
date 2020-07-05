#inner function as a function name

def the_number(num):
    def the_power(po):
        return num ** po
    return the_power

obj=the_number(5)
print(obj(3))


# inner function as a function

def the_number(num):
    def the_power(po):
        return num ** po
    return the_power(2)

obj=the_number(5)
print(obj)