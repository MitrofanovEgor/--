from functools import reduce

a = [0,45,2094,5,64,47,24,2,40,23,678]
print(reduce(max,a))
print(reduce(min, a))
d = 0
for elem in a:
    if elem > 0:
        d += 1
print(d)
print(a.count("0"))