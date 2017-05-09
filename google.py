import math 
print("Welcome to the area finder calculator. Which shape would you like to find the area of? triangle, square, cirle, or trapezoid?")
equation = raw_input()
if(equation == "triangle"):
	print("what is the base of the triangle?")
	base = int(raw_input("base:"))
	print("what is the height of the triangle?")
	height = int(raw_input("height:"))
	trianglearea = (.5 * base * height)
	print("Area:")
	print(trianglearea)
if(equation == "square"):
	print("what is the base of the square?")
	base = int(raw_input("base:"))
	print("what is the height of the square?")
	height = int(raw_input("height:"))
	squarearea = (base * height)
	print("Area:")
	print(squarearea)
if(equation == "circle"):
    print("what is the radius of the circle?")
    radius = int(raw_input("radius:"))
    circlearea = (radius * radius * (math.pi))
    print("Area:")
    print(circlearea)
if(equation == "trapezoid"):
    print("what is the first base of the trapezoid?")
    firstbase = int(raw_input("first base:"))
    print("what is the second base of the trapezoid?")
    secondbase = int(raw_input("second base:"))
    print("what is the height of the trapezoid?")
    height = int(raw_input("height:"))
    trapezoidarea = ((firstbase + secondbase)/2 * height)
    print("Area:")
    print(trapezoidarea)




