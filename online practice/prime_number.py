def m3(num):
    f = 0
    for i in range(2,num):
        if num % i == 0:
            f =1
    if f ==0:
        print("it is a prime number ")
    else:
        print("it is not prime number")
m3(67)
