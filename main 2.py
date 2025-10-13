#use pi from math library
import math 

#define radius and turn radius into a float variable
radius= input("Enter the radius: ")
print ("The radius is", radius)
radius=float(radius)

#calculate circumference
circumference = 2 *math.pi *radius
print (f"The circumference is {circumference}")

#calculate area
area =  math.pi * (radius **2)
print (f"The area is {area}")