def o5(ip_year):
    if (ip_year % 400 == 0):
        print("{}is a Leap Year".format(ip_year))
    elif (ip_year % 100 == 0):
        print("{} is Not the Leap Year".format(ip_year))  # leap year
    elif (ip_year % 4 == 0):
        print("{} is a Leap Year".format(ip_year))
    else:
        print("{} is Not the Leap Year".format(ip_year))


o5(1900)
