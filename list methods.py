a = [1,2,3,4,5,]
print(a.append(12))
print(a.count(1))
print(a.insert(5,[78475,454783,3324]))
print(a.extend([9,3,5,6,7]))
print(a.clear)

print(a)
b =a[::]
print(b)
a.extend([74747])#deep copy
print(b)
print(a)
