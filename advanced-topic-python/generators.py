def gen():
    n=1
    print("I am first")
    yield n
    
    n+=1
    print('I am second')
    yield n
    
    n+=1
    print('I am third')
    yield n

poo=gen()
for i in poo:
    print(i)