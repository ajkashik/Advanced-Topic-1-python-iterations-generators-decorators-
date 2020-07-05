step=[1,4,0,7,8]
my_iter=iter(step)
print(next(my_iter))
print(next(my_iter))
print(my_iter.__next__())
print(my_iter.__next__())
print(next(my_iter))
