def m6(fn,sn,tn):
    if fn >= sn and fn >= tn :
        print("{} is the greatest number".format(fn))
    elif sn >= fn and sn >= tn :
        print("{} is the greatest number".format(sn))
    elif tn >= sn and tn >= fn :
        print("{} is the greatest number ".format(tn))
m6(22,31,13)