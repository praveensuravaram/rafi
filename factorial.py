def fact(num):
    if num==1: 
        return num
    else:
        return num*fact(num-1)
        
num=int(input("enter the number"));
if num<0:
    print("factorial is doesnot exit for th negative values")
elif num==0:
    print("factorialm for 0 is 1")
else:
    print("factorial for",num,"is", fact(num))
