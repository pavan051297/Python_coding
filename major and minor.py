 task 3
dob=(input("date of birth dd/mm/yy:-"))
x=dob.split("/")
diff=2021-int(x[2])
if diff >18:
    print("you are major")
elif diff < 16:
    print("you are minor")
elif diff ==17:
    if int(x[1])<11:
         print("this month born")
    if int(x[1]) == 1:
        print("born in jan")
    elif int(x[1]) == 2:
        print("feb")
    elif int(x[1]) == 3:
        print("mar")
    elif int(x[1]) == 4:
        print("april")
    elif int(x[1]) == 5:
        print("may")
    elif int(x[1]) == 6:
        print("june")
    elif int(x[1]) == 7:
        print("born in july")
    elif int(x[1]) == 8:
        print("aug")
    elif int(x[1]) == 9:
        print("sep")
    elif int(x[1]) == 10:
        print("oct")
    elif int(x[1])==11:
           print(("nov"))
           if int(x[0])<11:
               print("she is minor")
           if int(x[0])>=11:
               print("she is  major")

    elif int(x[1])==12:
        print("she is still minor")

# type 3

dob = (input("date of birth dd/mm/yy:-"))
c = 11 / 11 / 2022
x = dob.split("/")
diff = 2021 - int(x[2])
if diff > 18:
    print("you are major")
elif diff < 17:
    print("you are minor")
elif diff == 17:
    print("she is minor but")
    if int(x[1]) == 1:
        print("born in jan")
    elif int(x[1]) == 2:
        print("feb")
    elif int(x[1]) == 3:
        print("mar")
    elif int(x[1]) == 4:
        print("april")
    elif int(x[1]) == 5:
        print("may")
    elif int(x[1]) == 6:
        print("june")
    elif int(x[1]) == 7:
        print(" july")
    elif int(x[1]) == 8:
        print("aug")
    elif int(x[1]) == 9:
        print("sep")
    elif int(x[1]) == 10:
        print("oct")
    elif int(x[1]) == 11:
          if int(x[o])>10:
              print("not yet major")
          elif int(x[0])>=11:
              print("she will major in next 50 days")
print()

