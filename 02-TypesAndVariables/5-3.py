a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))

volume = a*b*2 + a*c*2 + b*c*2
surface_area = a*b*c
print(f'The volume is {volume}')
print(f'The surface area is {surface_area}')