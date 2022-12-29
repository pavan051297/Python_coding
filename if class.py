a=input("name if the class")
if a=="history":
    print("history class ")
    name =input("name of the teacher")
    if name=="pavan":
        print("deals with 1 unit")
    elif name=="mohan":
        print("dels with 2 unit")
        exit()
elif a == "maths":
     teacher=input("1.p\n2.r\n3.f \nenter your chioce")
     if teacher=="p":
         print("its is pt class")
     if teacher=="r":
         print("it is rest class")
     if teacher=="f":
         print("it is fun class")
elif a != "maths ,history":
    a = input("1.lab\n2.sports\n3.food\n choose the class")
    if a==("lab"):
        print (len("python"))
    if a == ("sports"):
        print((3**3))
    if a==("food"):
        print(a[0:3])




