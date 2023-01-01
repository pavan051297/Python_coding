string_1 = "pavan new project"
result =''
vowels = ("a","A","e","E","i","I","o","O","u","U")
for i in string_1:
    if i in vowels:
        i= i.upper()
    result += i
print(result)