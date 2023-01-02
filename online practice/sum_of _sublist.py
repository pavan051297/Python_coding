a = [-2,1,-3,8,4,-1,2,1,-5,4]
c = 0
s = 0
for j in range(len(a)):
    for i in range(len(a)):
        b =sum(a[i:i+1+j])
        if b > c:
            c = b
print(c)
