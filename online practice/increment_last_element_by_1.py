a = [1,2,3]
for i in range(len(a)):
    if a[i] == len(a):
        value = a[i]+1
        c.append(value)


    else:
        value = a[i]
        c.append(a[i])
print(c)