import math
print("          ##### AREA OF A SHAPE #####          ")
print("Select A Shape")
print("1. Rectangle\n2. Triangle \n3. Circle")
input_from_user = input("Enter the selection (1/2/3):")
input_value = int(input_from_user)
if (input_value == 1):
    input_lenght = input("Enter Lenght:")
    input_width = input("Enter Width:")
    input_lenght = int(input_lenght)
    input_width = int(input_width)
    if (input_lenght == input_width):
        print("The Rectangle is a Square with area:")
        area = input_lenght*input_width
        print(area)
    else:
        print("The Area of the Rectangle is:")
        area = input_lenght*input_width
        print("Area:",area)
elif (input_value == 2):
    input_h = input("Enter height:")
    input_b = input("Enter base:")
    input_h = int(input_h)
    input_b = int(input_b)
    print("The Area of the triangle is:")
    area = (0.5*input_h*input_b)
    print(area)
elif (input_value == 3):
    input_r = input("Enter Raduis of Circle:")
    input_r = int(input_r)
    print("The Area of the Circle is:")
    area = (math.pi*input_r*input_r)
    print(area)
else:
    print("Wrong Option Selection")