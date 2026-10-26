def sum_digits(number):
    number_abs = abs(number)
    number_str = str(number_abs)
    total=0
    for digit in number_str:
        total += int(digit)
    return total

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')