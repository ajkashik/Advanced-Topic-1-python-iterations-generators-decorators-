def animal(num):
    n=len(num)
    for i in range(n):
        yield num[i]
        
        
for e in animal("pandas"):
    print(e)