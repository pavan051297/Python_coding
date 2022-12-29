# a="hello world "
# print((a))


#  task 2
# num1=int(input("choose the number "))
# num2=int(input("choose number "))
# operations=input("1.add\n2.sub\n3.multi\n4.div\nchoose the operation:=-")
# if operations=="add":
#     print(num1+num2)
# if operations=="sub":
#     print(num1-num2)
# if operations=="multi":
#     print(num1*num2)
# if operations=="div":
#     print(num1/num2)
# task 3
# swap number

# p=int(input("choose the number"))
# q=int(input("choose the number"))
# r=p
# p=q
# q=r
# print(p,q)


# a=int(input("choose km"))
# print(a*0.65432)

# import calendar
# a=int(input("choose year"))
# b=int(input("choose month"))
# print(calendar.month(a,b))


# a=int(input("choose the number"))
# if a==0:
#     print("value is zero")
# elif a<0:
#     print("value is negative")
# elif a>0:
#     print("value is positive")


# task 4
# a=int(input("choose the number"))
# if a%2==0:
#     print("it is even")
# else:
#     print("it is odd")


# task 5
# a=int(input("choose the number"))
# if a%400==0:
#     print("it is leap")
# elif a%100==0:
#     print("it is not leap")
# elif a%4==0:
#     print("it is leap")


# task 5
# for i in range(2,101):
#    f=0
#    for j in range(2,i-1):
#     if i%j == 0:
#        f=1
#    if f==0:
#        print("{} it is a prime number".format(i))
#    else:
#        print("{} it is not prime".format(i))
#
# for i in range(1,21):
#    for j in range(1,11):
#        c=i*j
#        print("{}*{}={}".format(i,j,c))
#    print()
# def fib(n):
#     if n<2:
#         print("bdzbdshb")
#     a=0
#     b=1
#     print(a)
#     print(b)
#     for i in range(2,n):
#       c=a+b
#       a=b
#       b=c
#       print(b)
# fib(20)



for i in range(0,4):
    for j in range(0,4):
        print(j,end="")
    print()