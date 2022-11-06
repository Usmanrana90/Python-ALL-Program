n =int(input('Enter the number:'))
f=1
i=1
if n%5!=0:
    while i<=n:
        f=f*i
        i=i+1
    print(f)