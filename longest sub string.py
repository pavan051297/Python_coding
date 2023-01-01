# def st(str):
#   le = len(str)
#   op = ""
#   new = ""
#   for i in range(len(str) - 1):
#     if str[i] not in op :
#         op = op + str[i]
#         if i == len(str) - 1:
#             if op > new:
#                new = op
#     else:
#         if op > new:
#            new = op
#            op = str[i]
#         else:
#             op = str[i]
#
# b = st("abcabcdafsweraumbrella")
# print(st)




# st = "abcbcdahmnbvfghjkloiu"
# op = ""
# ls = []
# for i in range(len(st)):
#     if st[i] not in op :
#         op = op+st[i]
#         if i == (len(st) -1):
#             ls.append(op)
#     else:
#         ls.append(op)
#         op = st[i]
# print(ls)


def finding_greatest_substring(st):
    great = ""
    op = ""
    ls = []
    for i in range(len(st)):
        if st[i] not in op:
            op = op + st[i]
            if i == (len(st) - 1):
                ls.append(op)
        else:
            ls.append(op)
            op = st[i]

    print(ls)


finding_greatest_substring("jsdfhsdkhfusrfhksfkmvsf")
finding_greatest_substring("sdjfbdsbfjdsbff")
finding_greatest_substring("sdfjdsbfmbdsjhfbds")
