def m1(n):
    s = str(n)
    count = 0
    for i in s:
       c = int(i)**3
       count += c
    return count
print(m1(371))






def m2(n):
    count = 0
    while (n != 0):
      res = n %10
      count = count+res*res*res
      n = n //10
    return count
print(m2(371))