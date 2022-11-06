print("{:%^8}".format("RAM"))   #format  #1
print("{:*^5.3}".format("gatenetacademy"))  #2



person={'age':48,'name':'shiva'} #3

print("{p[name]}'s age is :{p[age]}".format(p=person))  #p ki jegah***


num="{:{align}{width}.{precision}f}"  #4

print(num.format(123.456,align='<',width=8,precision=2))  #precesion point k bad digit

import datetime   #5

d=datetime.datetime.now()
print("it's now :{:%d/%m/%y %H:%M:%S}".format(d))

c=1+2j    #6
print("Real Part:{0.real} and img part:{0.imag}".format(c))


l=[10,10,20,30,40,20,"usm"]   #7
l[2]=100
print(l[2])