max_num = 15
num_gen = (num for num in range(1, max_num + 1, 2))

print(next(num_gen))
print(next(num_gen))
print(next(num_gen))
print(next(num_gen))
print(*num_gen)
print(type(num_gen))