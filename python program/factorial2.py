n =int(input('Enter the number:'))
f=1
i=1
for m in range(1,n+1): #1,2,3,4 factorial
    while i<=m:
        f=f*i
        i=i+1
    print("Factorial",f)