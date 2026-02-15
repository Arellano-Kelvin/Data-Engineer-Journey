def greet(name):
    return f'Hello {name}'
def if_even(number):
    return number % 2 == 0
def calculate_area(length, width):
    if length > 0 and width > 0:
        return length * width
    else:
        print('Please input valid number')
def find_max(list_of_numbers):
    if len(list_of_numbers) == 0:
        return None
    return max(list_of_numbers)

def validate_age(age):
        try:
            if 120 >= age >= 0:
                return age<=120
        except TypeError:
            age = 0