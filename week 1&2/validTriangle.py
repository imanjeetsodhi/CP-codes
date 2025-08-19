# given 3 integer angles of triangle tell wether the triangle is valid or not

angle1 = int(input("enter the first angle : "))
angle2 = int(input("enter the second angle : "))
angle3 = int(input("enter the thried angle : "))

if angle1 > 0 and angle2 > 0 and angle3 > 0 and (angle1 + angle2 + angle3 == 180):
    print("The triangle is valid.")
else:
    print("The triangle is NOT valid.")
