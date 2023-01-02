def m5(num):
    count = 0
    while num  > 0:
        digit = num % 10
        count = count*10 + digit
        num = num //10
    print(count)

m5()