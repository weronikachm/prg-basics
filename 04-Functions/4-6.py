def day_name(day_number):
    result = ''
    if day_number == 1:
        result = 'Monday'
    elif day_number == 2:
        result = 'tuesday'
    elif day_number == 3:
        result = 'wednesday'
    elif day_number == 4:
        result = 'thursday'
    elif day_number == 5:
        result = 'friday'
    elif day_number == 6:
        result = 'saturday'
    else: 
        result = 'sunday'
    return result

print('The name of day 5 in the week is', day_name(5))
print('The name of day 3 in the week is', day_name(3))
print('The name of day 7 in the week is', day_name(7))