def n3(n):
    for i in range(1,n+1):
        if  n % i == 0:
           print(i)
n3(26)




def n4(number):
    flag = 1
    summ = 0
    for i in range(1,number+1):
        flag = flag*i
        summ += flag
        print(flag)