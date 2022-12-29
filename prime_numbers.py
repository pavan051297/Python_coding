for k in range(2, 100):
    f = 0
    for i in range(2, k - 1):
        if (k % i) == 0:
            f = 1

    if f == 0:
        print("{} is prime number".format(k))
    else:
        print("{} is  a prime number".format(k))