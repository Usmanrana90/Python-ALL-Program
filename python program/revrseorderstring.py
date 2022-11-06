s=input('enter some string : ')
s1=s.split()
print(s1)
l=[]
i=0
while i<len(s1):
    l.append(s1[i][::-1])
    i=i+1
output=' '.join(l);
print(output)