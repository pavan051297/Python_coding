def n1(num):
    sum = 0
    for i in range(1,(num//2)+1):
        res = num % i
        if res == 0:                                                              
           sum = sum + i
    if sum == num :
        print(" {} is perfect number".format(num))
    else:
        print("{} is not a perfect number".format(num))
n1(43)