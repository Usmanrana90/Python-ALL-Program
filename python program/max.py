a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))

if(a<b)and(a<c):
 print("Min is:",a)
elif(b<a) and (b>c):
 print("Min is:",b)
elif(c<a) and (c>b):
 print("Min is:",c)
