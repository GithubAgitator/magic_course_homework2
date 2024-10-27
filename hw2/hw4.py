lst = ['Hello', 1, '7', True, False, 5.4, (1,)]
d = {}
for i in lst:
    k = type(i)
    if k not in d:
        d[k] = []
    d[k].append(i)
print(d)










