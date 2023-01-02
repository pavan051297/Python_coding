def n8(base,top):
                                                                   # pow
      print(pow(base,top))
n8(2,3)


def n9(base,power):
      count = 1                                                                        #pow
      for i in range(power):
        count =count * base
      print(count)

n9(2,3)


def o1(b,e):
    res =1                                                                              # pow
    while e != 0:
       res = b * res
       e  -= 1
    print(res)
o1(2,3)


def o2(a):
     s  = a*a
     c = a*a*a
     return s,c                                                                            #sruare and cube
print(o2(2))


def o3(si,i,t):
    print((si*i*t)/100)                                                             #simple interest
o3(1000,300,5)












def o4(F):
    c  = ((F - 32)*5)/9
    return c
print(o4(98.0))



def o5(C):
    v = (C *1.8) + 32                                                              #c
    return v

print(o5(32))