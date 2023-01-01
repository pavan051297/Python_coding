def n7(fn,sn,tn):
    if fn <= sn and fn <= tn :
        print("{} is the smallest number".format(fn))
    elif sn <= fn and sn <= tn :
        print("{} is the smallest number".format(sn))                             # smallest number
    elif tn <= sn and tn <= fn :
        print("{} is the smallest number ".format(tn))

n7(22,78,3)
