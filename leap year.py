# task 1
# n=int(input("select a year"))
# for i in range(1900,2022,4):
#     if n==i:
#         print("{} is a leap year".format(i))
#
# task 2
# year=int(input("select a year:-"))
# if year %4==0:
#     print("{}  leap year".format(year))
# else:
#     print("{}   is not leap year".format(year))


# task 3
for input_year in range(1900,2023):
      if (input_year%400 == 0):
          print("{}is a Leap Year" .format(input_year))
      elif (input_year%100 == 0):
          print("{} is Not the Leap Year".format(input_year))
      elif (input_year%4 == 0):
        print("{} is a Leap Year" .format(input_year))
      else:
        print("{} is Not the Leap Year" .format(input_year))

#




#
# for num  in range(1900,2023):
#     if num  %  4 == 0:
#         if num  %  100 == 0 and num  %  400 == 0:
#             print("{}  is leap year ".format(num))
#         elif num % 100 == 0:
#             print("{} is leap year".format(num))
#         else:
#             print("{} is  not leap year".format(num))
#     else:
#         print("it is not leap year ")



