a = "pavandhjvhyd"
result =""
r =('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
for s in a:
    if s in r:
        s = ""
    result += s
print(result)