import math 
def circumference(radius):
    circumference=(2*math.pi*radius)
    return circumference

radius= int(input("choose the radius of the circle: "))
print ("The circumference of the circle with your chosen radius is: ",circumference(radius))
