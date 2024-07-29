def Areaofcircle():
    diameter = int(input("What is the diameter of the Circle in cm? "))
    radius = diameter/2
    Acircle = 3.142 * radius * radius
    return Acircle

Area = Areaofcircle()
print("The area of the circle is", Area,"cmsquared")
