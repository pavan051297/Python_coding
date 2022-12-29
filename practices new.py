# question 1
# a = int(input("choose a number"))
# sum = 0
# b = str(a)
# for i in b:
#     op = int(i)**len(b)
#     sum += op
# if sum == a:
#     print("its is amstrng")
# else:
#     print("it is not")

    # question
def primenumber(n):
    f =0
    for i in range(2,n-1):
        if n % i ==0:
            f = 1
    if f == 0:
        print("it is prime")
    else:
        print("it is not prime")
primenumber(100)