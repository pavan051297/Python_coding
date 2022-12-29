ip = ["9.3.2.1","350.2.1.3","2.3.1","6.7.8.3","9.a.0.1","2.*.1.2","9.4.5.2"]

for i in ip:

    if len(i.split('.')) != 4:
        continue
    else:
        octets = i.split() #
        is_ip = True
        for o in octets:
            if o.isdigit():
                n = int(o)
                if 0 < n < 256:
                    continue
                else:
                    is_ip = False
            else:
                is_ip = False
        if is_ip:
            print("{} is valid ip address".format(i))