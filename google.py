import math 
print("Welcome to the area finder calculator. Which shape would you like to find the area of? triangle, square, circle, or trapezoid?")
equation = raw_input()
if(equation == "triangle"):
	print("what is the base of the triangle?")
	base = float(raw_input("base:"))
	print("what is the height of the triangle?")
	height = float(raw_input("height:"))
	trianglearea = (.5 * base * height)
	print("Area:")
	print(trianglearea)
if(equation == "square"):
	print("what is the base of the square?")
	base = float(raw_input("base:"))
	print("what is the height of the square?")
	height = float(raw_input("height:"))
	squarearea = (base * height)
	print("Area:")
	print(squarearea)
if(equation == "circle"):
    print("what is the radius of the circle?")
    radius = float(raw_input("radius:"))
    circlearea = (radius * radius * (math.pi))
    print("Area:")
    print(circlearea)
if(equation == "trapezoid"):
    print("what is the first base of the trapezoid?")
    firstbase = float(raw_input("first base:"))
    print("what is the second base of the trapezoid?")
    secondbase = float(raw_input("second base:"))
    print("what is the height of the trapezoid?")
    height = float(raw_input("height:"))
    trapezoidarea = ((firstbase + secondbase)/2 * height)
    print("Area:")
    print(trapezoidarea)




