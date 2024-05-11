mark = input().split(" ")

M = int(mark[0]) #月份
D = int(mark[1]) #天數

S=(M*2+D)%3


# print("M=",M)
# print("D=",D)
# print("S=",S)

if(S==0):
    print("普通")
elif(S==1):
    print("吉")
else:
    print("大吉")