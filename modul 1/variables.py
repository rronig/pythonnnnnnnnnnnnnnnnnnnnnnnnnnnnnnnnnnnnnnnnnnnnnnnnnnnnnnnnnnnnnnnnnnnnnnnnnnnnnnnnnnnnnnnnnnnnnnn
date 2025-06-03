temperature = 20
name = "John"
print(temperature, '\n'+name)
print(type(temperature))
print(type(name))

x=12
b=43
a=x+b
y=x-b
z=x*b
p=x/b
print(x,b,a,y,z,p)
a=12
first="John"
last="Doe"
print(first,last)
def dsa(a, b):
    p=str(a)+str(b)
    print(p)
n1=int(input("Number 1:"))
n2=int(input("Number 2:"))
dsa(n1,n2)
def is_even(n):
    if n % 2 == 0:
        print(True)
    else:
        print(False)
is_even(int(input("123:")))