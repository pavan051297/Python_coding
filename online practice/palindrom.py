def s4(string):
    if string[::] == string[::-1]:
        print("it is palindrom")
    else:
        print("it is not a palindrom")
string = "ppaavvaapp"
s4(string)
