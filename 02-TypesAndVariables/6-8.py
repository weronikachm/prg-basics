first = input('Enter first letter: ')
last = input('enter last letter: ')
first_letter_code = int(ord(first))
last_letter_code = int(ord(last))
number_of_letters = last - first -1
print(f'Between {first} and {last} is {number_of_letters} letters')