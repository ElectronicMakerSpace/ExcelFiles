a = [1,2,3,4,5]
b = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(a) + 1):
    for j in range(1, len(b) + 1):
        print(f'{j},{i}')