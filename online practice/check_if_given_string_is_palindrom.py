st ="malayalam"
for i in range(len(st)):
    if st[i] == st[len(st)-1-i]:

       print("{}  and {}  are same so lt is palindorem".format(st[i],st[len(st)-1-i]))
    else:

        print("it is not")
