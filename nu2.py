a = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
for i in range(len(a) - 1):
    b = [a[i]]
    i += 1
    c = [a[i]]
    if c > b:
        b = c
        print(b)