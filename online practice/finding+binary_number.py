def m7(num):
    while num > 0 :
        j = num % 10
        if j != 0 or j != 1:
            print("{} is not  a binary".format(num))
            break
        num = num // 10
        if num == 0:
            print("it is a binary")
m7(100101)