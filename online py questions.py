
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
#         numbers = int(input())                                 #avg of number
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
# n4(24)


# def n5(numbers):
#       while numbers >= 0:
#           if numbers % 2 == 0:
#               print("{} is is even number ".format(numbers))                            #odd and even number
#           else:
#               print("{} is odd number ".format(numbers))
#           break
#
# n5(32)
#

# def n6(first):
#     for j in range(1,first):
#         f = 0
#         for i in range(2,j):
#             if j  % i == 0:
#                 f =1
#         if f ==0:
#             print("{} is a prime number ".format(j))             # Write a program in Python to check n prime  numbers
#         else:
#              print("{} is not prime number".format(j))
#
# n6(43)


# def n7(fn,sn,tn):
#     if fn <= sn and fn <= tn :
#         print("{} is the smallest number".format(fn))
#     elif sn <= fn and sn <= tn :
#         print("{} is the smallest number".format(sn))                             # smallest number
#     elif tn <= sn and tn <= fn :
#         print("{} is the smallest number ".format(tn))
#
# n7(22,78,3)


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



# def o5(input_year):
#       if (input_year%400 == 0):
#           print("{}is a Leap Year" .format(input_year))
#       elif (input_year%100 == 0):
#           print("{} is Not the Leap Year".format(input_year))                     #leap year
#       elif (input_year%4 == 0):
#         print("{} is a Leap Year" .format(input_year))
#       else:
#         print("{} is Not the Leap Year" .format(input_year))
# o5(1900)






                                   # string codes
# def S1(char):
#      # char = "s"
#      st ="Hello worls my name is pavan\n"
#      lt = list(st)
#      for i in lt:                                                  #removing specified char
#         if i != char:
#             print("".join(i),end="",)
#
# def s2(ch):
#     st = "Hello worls my name is pavan"
#     st.replace(ch,"")                                                         #another simple way:
#     print( st)
#
#
# S1("r")
# s2("p")


# def s3(string,cha):
#     count = 0
#     for i in range(len(string)):
#         if (string[i] == cha):                                               #occarence of a character
#             count = count +1
#     print(count)
# string = "Hello world i am poavan"
# cha = "o"
# s3(string,cha)

#
# a = "care"
# b = "race"
# if len(a) == len(b):
#     for i in range(len(a)):
#         if a[i]   in b[::]:
#             # i = i +1
#
#
#             print("it is   anagram")
#
#
#         else:
#             print("it is not anagram")
#


# def s4(string):
#     if string[::] == string[::-1]:
#         print("it is palindrom")                             #palindrom
#     else:
#         print("it is not a palindrom")
# string = "ppaavvaapp"
# s4(string)



# def s5(cha):
#     vowels = ("a","A","e","E","i","I","o","O","u","U")
#     if cha in vowels :
#         print('it is a vowel')
#     else:
#         print("it is not vowel")
#
# s5("a")
#


# def s6(chas):
#     print(chas.isdigit())
#     for cha in chas:
#         if cha >= str(0) and cha <= str(9) :
#             print("it is digit")                                                 #is digit or not
#     else:
#         print("it is ")
# chas = input("choose a char:-")
# s6(chas)

#
# a  = "hello world i am pavan"
#
# print(a.replace(" ","a"))
#

# a ="pavan new project"
# print(a.upper())
# result =""
# for i in a:
#     i= i.upper()                                                   #uppercase
#     result += i
# print(result)


# string_1 = "pavan new project"
# result =''
# vowels = ("a","A","e","E","i","I","o","O","u","U")           #converting vowles into uppercase
# for i in string_1:
#     if i in vowels:
#         i= i.upper()
#     result += i
# print(result)


# string = "pavan new project"
# vowels = ("a","A","e","E","i","I","o","O","u","U")
# result = ''
# for i in string:                                              #removing vowles in string
#     if i in vowels:
#         i =''
#     result += i
# print(result)


# string = "pavan new project"
# vowels = ("a","A","e","E","i","I","o","O","u","U")
# count = 0
# for i in string:
#     if i in vowels:
#         i = 1
#         count += i
# print(count)



# string = "pavan new project"
# vowels = ("a","A","e","E","i","I","o","O","u","U")
# vowel = 0
# consonent =0
# for i in string:
#      if i in vowels:
#          vowel +=1                                                      #count of vowels and consonents
#      elif i.isalpha():
#          consonent += 1
# print("total no of characters in the string is",len(string))
# print("vowels in the given string is ",vowel)
# print("consonents in the given string",consonent)


i = "paapaag fueogidion"
count = {}.fromkeys(i, 0)

for char in i:
    if char in count:
         count[char] += 1
print(i,count)
print(max(i,key =count.get))

















