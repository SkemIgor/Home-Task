def generator(max_num):
    for i in range (1, max_num + 1, 2):
        yield i

num_gen = generator(39)
print(next(num_gen))
print(next(num_gen))
print(next(num_gen))
print(*num_gen)
print(type(num_gen))