#practice problems
a=int(input("Enter a number: "))
b=int(input("Enter b number: "))
c=a+b
print("The sum of a and b is: ", c)

# the area of a rectangle 
length=float(input("Enter the length: "))
width=float(input("Enter the width: "))
area=length*width
print("The area of the rectangle is: ", area)

#the area of a circle 
radius=float(input("Enter the radius: "))
area=3.14*radius**2
print("The area of the circle is: ",area)

#change temperatue from celsius to fahrenheit 
celsius=float(input("Enter the temperature in celsius: "))
fahrenheit=(celsius*9/5)+32
print("The temperature in fahreheit is: ", fahrenheit)

#swappimg variables
a=5
b=10
temp=a
a=b
b=temp
print(a)
print(b)