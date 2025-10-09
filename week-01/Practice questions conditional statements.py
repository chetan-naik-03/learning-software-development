#WAP to check if a number entered by a user is even or not
num = int(input("enetr a number = "))

rem  = num % 2

if(rem == 0):
    print("EVEN")
else :
    print("ODD")   

#WAP  to find the greatest of 3 numbers entered
a = int(input("eneter first number ="))
b = int(input("eneter second number ="))
c = int(input("eneter third number ="))

if(a>=b and a>=c):
    print("first number is greater", a)
elif(b>=c):
    print("second number is the largest", b)
else :
    print("Third number is the largest", c)    

#WAP to show that a number is a multiple of 7 or not
a = int(input("enter the number = "))


if(a%7 == 0):
    print("Yes it's a multiple of 7")
else :
    print("no it's not multiple of 7")


