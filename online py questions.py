
# def m1(n):
#     s = str(n)
#     count = 0
#     for i in s:
#        c = int(i)**3                     #Write a program in Python to check whether an integer is Armstrong number or not.
#        count += c
#     return count
# print(m1(371))
#
#
#
#
# def m2(n):
#     count = 0
#     while (n != 0):
#       res = n %10
#       count = count+res*res*res                    #Write a program in Python to check whether an integer is Armstrong number or not.
#       n = n //10
#     return count
# print(m2(371))
#
# #

# def m3(num):
#     f = 0
#     for i in range(2,num):
#         if num % i == 0:
#             f =1
#     if f ==0:
#         print("it is a prime number ")     # Write a program in Python to check given number is prime or not.
#     else:
#         print("it is not prime number")
# m3(67)



# def m4(num):
#     a = 0
#     b = 1
#     print(a)
#     print(b)
#     for i in range(2,num+1):                                                                #fid
#        c = a + b
#        a = b
#        b = c
#        print(c)
# m4(25)

# def m5(num):
#     count = 0
#     while num  > 0:
#         digit = num % 10
#         count = count*10 + digit                                                     #palindrom
#         num = num //10
#     print(count)
#
# m5(786)

# def m6(fn,sn,tn):
#     if fn >= sn and fn >= tn :
#         print("{} is the greatest number".format(fn))
#     elif sn >= fn and sn >= tn :
#         print("{} is the greatest number".format(sn))                             # greatest number
#     elif tn >= sn and tn >= fn :
#         print("{} is the greatest number ".format(tn))
# m6(22,31,13)



# def m7(num):
#     while num > 0 :
#         j = num % 10
#         if j != 0 or j != 1:
#             print("{} is not  a binary".format(num))                             # finding binary number
#             break
#         num = num // 10
#         if num == 0:
#            print("it is a binary")
# m7(100101)



# def m8(a,b):
#      a = a - b
#      b = a + b
#      a = b - a                                                          #swaping withot third varible numbers
#      print("after swaping value of  a is {}".format(a))
#      print("after swaping  value of b is {}".format(b))
# m8(9,6)



# def m9(first,second):
#     temp = first
#     first = second                                                             #swaping with  3 varable
#     second = temp
#     print("first number is" ,first)
#     print("second number  is ", temp)
#
# m9(66,99)




# def n1(num):
#     sum = 0
#     for i in range(1,(num//2)+1):
#         res = num % i
#         if res == 0:                                                               #prefect number
#            sum = sum + i
#     if sum == num :
#         print(" {} is perfect number".format(num))
#     else:
#         print("{} is not a perfect number".format(num))
# n1(6)



# def n2(n):
#     ls = []
#     for i in range(n):
#         numbers = int(ip())                                 #avg of number
#         ls.append(numbers)
#     print(ls)
#     avg = sum(ls)/len(ls)
#     print(avg)
# n2(4)


# def n3(n):
#     for i in range(1,n+1):                                    # factors of a number
#         if  n % i == 0:
#            print(i)
# n3(26)


# def n4(number):
#     flag = 1
#     summ = 0
#     for i in range(1,number+1):                                                      #factorial
#         flag = flag*i
#         summ += flag
#         print(flag)
#







# def n8(base,top):
#                                                                    # pow
#       print(pow(base,top))
# n8(2,3)


# def n9(base,power):
#       count = 1                                                                        #pow
#       for i in range(power):
#         count =count * base
#       print(count)
#
# n9(2,3)


# def o1(b,e):
#     res =1                                                                              # pow
#     while e != 0:
#        res = b * res
#        e  -= 1
#     print(res)
# o1(2,3)
#

# def o2(a):
#      s  = a*a
#      c = a*a*a
#      return s,c                                                                            #sruare and cube
# print(o2(2))


# def o3(si,i,t):
#     print((si*i*t)/100)                                                             #simple interest
# o3(1000,300,5)


# def o4(F):
#      c  = ((F - 32)*5)/9                                                              #F
#      return c
# print(o4(98.0))



# def o5(C):
#     v = (C *1.8) + 32                                                              #c
#     return v
#
# print(o5(32))









                                   # string codes
#


#
#
#
#










#
#


#


#

#


#



#

#

#
#








# a = [1,2,4]
# b = [1,3,5]
# c =[]
# a.extend(b)
# print(sorted(a))


