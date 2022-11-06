n =int(input('Enter the number'))
sum=0
while n>0:
        r=n%10
        if r!=0:
            n=n//10
            if r%7!=0:
               sum=sum+r
            
print(sum)