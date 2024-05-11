mark = input()

# print("mark=",mark)


length = len(mark)

# print("length=",length)

if(len(mark) == 1):
    print("yes")
else:
    flag = 0
    for i in range(length//2):
        # print("i=",i,"mark[i]=",mark[i])
        # print("i=",length-i-1,"mark[i]=",mark[length-i-1])
        if(mark[i] != mark[length-i-1]):
            print("no")
            break
        else:
            flag = 1


    if(flag == 1):
        print("yes")
