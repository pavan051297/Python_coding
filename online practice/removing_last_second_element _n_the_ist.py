l = [1,2,3,4,5,6,7]
r  = []
print(len(l))
for i in range(len(l)):
    if l[i]  == len(l)-1:
        print(l[i])

    else:
        r.append(l[i])
print(r)
