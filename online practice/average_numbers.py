def n2(n):
    ls = []
    for i in range(n):
        numbers = int(input(""))
        ls.append(numbers)
    print(ls)
    avg = sum(ls)/len(ls)
    print(avg)
n2(4)