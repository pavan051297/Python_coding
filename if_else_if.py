city = input("Pls enter the city name:- ")

if city == "Hyderabad":
    print("You are Telangana state")
    pin = input("Pls enter your pincode")
    if pin == "5001":
        print("You are in Hitech City 1")
    elif pin == "5002":
        print("You are in Hitech City 2")
        area = "Kondapurr"
        if area == "madhapur":
            print("He is in madhapur")
        elif area == "Kondapur":
            print("in knodapur ")
        else:
            print("not in madhapur nor in kondapur")
            # if state
            #     jdsdjs
            #     if djks
            #         ddjsd
    elif pin == "5003":
        print("You are in Hitech City 3")


elif city == "vijayawada":
    print("You are in AP state")
elif city == "vijayawada":
    print("You are in Combined AP state")
elif city == "CHENNAI":
    print("You are in TN state")
else:
    print("You are not in South INDIA")

name = input("Enter Your name")

print(name)



task 2


 m=input("say your order:-")

# if m == "vada":
#     print("each vada price is 40")
#     type=input("which type:- ")
#     if type =="masala":
#         print("masala vada price is 50")
#     elif type=="plain":
#         print("plain is 42 $")
#     elif type=="both":
#         print("its is not avalilable")
# elif m == "puri":
#     print("each puri price is 30")
#     com=input("combination of puri with:-")
#     if com=="chatuny":
#         print("its free")
#     elif com=="sambar":
#         print("its 10$ extra")
# elif m =="bonda":
#     print("each bonda is 20")
# elif m =="dosa":
#     print("each dosa is 70")
# else:
#     r=input("request your requirement")



n = int(input(("choose the number:-")))
if n % 2 != 0:
    print("Werid")
elif n % 2 ==0:
    if n>= 2 and n<=5:
        print("Not Werid")
    elif n>=6 and n<=20:
        print("Weird")
    elif n > 20:
        print("Not werid")