x= -752
if x >0:
    reverse = 0
    while x > 0:
        digit = x % 10
        reverse = reverse * 10 + digit
        x = x // 10
elif x < 0:
    x = x * -1
    reverse = 0
    while x > 0:
        digit = x % 10
        reverse = reverse * 10 + digit
        x = x // 10
    reverse = reverse * -1
print(reverse)
