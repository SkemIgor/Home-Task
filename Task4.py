src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 45, 55, 4687, 346 ,546 ,46, 446, 146, 464]

res = [src[i] for i in range(1, len(src)) if src[i] > src[i-1]]
print(res)