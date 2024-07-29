Area = input("Which area do you want to calculate (square/triangle/rectangle/circle)?" )
if (Area.lower() == "square"):
    Length = int(input("What is the length of the square in cm?"))
    Asqr = Length * Length
    print("The Area of the Square is " + str(Asqr) +"cm squared.")
    
elif (Area.lower() == "triangle"):
    Height = int(input("What is the height of the Triangle in cm?"))
    Base = int(input("What is the baselenght of the Triangle in cm?"))
    Atri = 0.5 * Base * Height
    print("The Area of the Triangle is " + str(Atri) +"cm squared.")

elif (Area.lower() == "rectangle"):
    len = int(input("What is the length of the Rectangle in cm?"))
    Width = int(input("What is the width of the Rectangle in cm?"))
    Arec = len * Width
    print("The Area of the Rectangle is " + str(Arec) +"cm squared.")
    
elif (Area.lower() == "circle"):
    diameter = int(input("What is the diameter of the Circle in cm?"))
    radius = diameter/2
    Acircle = 3.142 * radius * radius
    print("The Area of the Circle is " + str(Acircle) +"cm squared.")


else:
    print("You have not selected an available shape.")



Area = input("Which area do you want to calculate (square/triangle/rectangle/circle)?")




 
