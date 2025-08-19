# Read three angles of triangles and determine their types(Right triangle, Obtuse triangle, Acute triangle).

angle1 = int(input("Enter first angle: "))
angle2 = int(input("Enter second angle: "))
angle3 = int(input("Enter third angle: "))

if(angle1 + angle2 + angle3 != 180):
    print("The angles not form triangle.")
elif (angle1 == 90 or angle2 == 90 or angle3 == 90):
    print("The is a Right triangle.")
elif (angle1 > 90 or angle2 > 90 or angle3 > 90):
    print("The is an Obtuse triangle.")
else:
    print("The is an Acute triangle.")