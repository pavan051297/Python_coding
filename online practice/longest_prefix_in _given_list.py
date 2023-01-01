strs = ["flower","flow","flight"]

f = strs[0]
s = strs[1]
t = strs[2]
c =""

for i in range(4):
    if f[i] == s[i] and f[i] == t[i]:
        c = c+f[i]
print(c)