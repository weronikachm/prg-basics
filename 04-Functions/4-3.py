import math
def triangle_area(a,b,c):
    s = (a+b+c)/2
    p = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return p
a = int(input("podaj 1 bok:"))
b = int(input("podaj 2 bok:"))
c = int(input("podaj 3 bok:"))
pole = triangle_area(a,b,c)
print(pole)


