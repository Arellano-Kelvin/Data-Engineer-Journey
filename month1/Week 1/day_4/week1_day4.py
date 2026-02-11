def greet(name):
    return f'Hello {name}'
def if_even(number):
    return number % 2 == 0
def calculate_area(length, width):
    if length > 0 & width > 0:
        return length * width
    else:
        print('Please input valid number')
def find_max(list_of_numbers):
    return max(list_of_numbers)
def validate_age(age):
    if len(age) >=0:
        try:
            return age<=120
        except TypeError:
            age = []
