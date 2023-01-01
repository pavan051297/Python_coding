def s3(string,cha):
    count = 0
    for i in range(len(string)):
        if (string[i] == cha):
            count = count +1
    print(count)
string = "Hello world i am poavan"
cha = "o"
s3(string,cha)
