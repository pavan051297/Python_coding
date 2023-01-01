def s6(chas):
    print(chas.isdigit())
    for cha in chas:
        if cha >= str(0) and cha <= str(9) :
            print("it is digit")
    else:
        print("it is ")
chas = ip("choose a char:-")
s6(chas)