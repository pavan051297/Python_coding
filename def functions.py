# def add(*a):
#     c = a[0]+a[1]
#     return c
# def sub(a,b):
#     d= a-b
# #     return d
# def multiple(*a,**b):
#     e= a[0]*b["c"]
#     return e
# def div(a=8,b=2):
#     f= a//b
#     return f
# print (add(7,8,89))


#
# print (multiple(5,c=4))
#
#
#
# # task 2
# def myfunction (*name):
#     print("this is " + name[1] )
#
# myfunction("pavan","yugesh","mohan")
#
#
#
# # task 3
# def city(x="hsdbh"):
#     print("my city ", x)
# city("mpl")
# city("tpt")
# city()


# def myFun(**kwargs):
#     for key, value in kwargs.items():
#         print("{} == {}" .format (key, value))
#
# myFun(first='Geeks', mid='for', last='Geeks')



# task 111
# def myfun(a,b=4,c=5):
#     return 2*a+3*b+4*c
# print (myfun(2))
# print(myfun(2,2,2))



# def square(x):
#     return  x*x
# print(square(3))


# def multi(a,b):
#     return a*b
# print(multi(square(3),4))


#
# def add(a,b):
#     operation = a+b
#     return operation



# def sub(a,b=5):
#     op = a-b
#     return  op


# def mul(*a,**b):
#     o = a[0]*b["c"]
#     return o


# def div(*a,b=6):
#     d =a[0]/b
#     return d
# print(add(2,3))
# print(sub(4))
# print(mul(10,1,c=2))
# print (div(9,6))



#
# def add(a, b):
#     s = a + b
#     return s
#
#
# result = add(2, 3)
# print("ths sum is {}".format(result))



#
#
# def multiplication(a,b):
#     m =a*b
#     return m
#
# result = multiplication(23,33)
# print("the multiplication is {}".format(result))






#task 33

def prime_number(a,b):
    for j in range(a,b):
        f = 0
        for i in range(2,j-1):
            if (j % i) == 0:
                f = 1

        if f == 0:
           print("{} is prime ".format(j))
        else:
            print("{} is not prime".format(j))


prime_number(2,100)


# task 23

# def multiplication(a,b):
#
#          for i in range(a,b):
#               for j in range(1,10):
#                    c = i*j
#                 print("{} * {} = {}".format(i,j,c))
#


# multiplication(1,21)


# task 24

# def fib(n):
#     if n < 2 :
#         print("number should be above 2")
#     a = 0
#     b = 1
#     print(a)
#     print(b)
#     for i in range(2,n+1):
#         c = a+b
#         a = b
#         b = c
#         print(a+b)
# fib(20)


# task 25
def amastrong(n):
    sum =0
    b = str(n)
    for i in b:
        op = int(i)**2
        sum +=int(op)
        print(sum)
amastrong(153)



