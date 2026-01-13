def area_and_perimeterof_rectangle(l, b):
    area = l * b
    perimeter = 2 * (l + b)

    return area, perimeter

l = int(input("Enter a length"))
b = int(input("Enter a breadth"))

print(area_and_perimeterof_rectangle(l,b))