def n6(first):
    for j in range(1,first):
        f = 0
        for i in range(2,j):
            if j  % i == 0:
                f =1
        if f ==0:
            print("{} is a prime number ".format(j))             # Write a program in Python to check n prime  numbers
        else:
             print("{} is not prime number".format(j))

n6(43)