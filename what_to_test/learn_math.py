# a simple math application
def add(x, y):
    return x + y

def substract(x, y):
    return x - y 

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError('Can not divide by zero')

    return x / y

add_operator = add(4, 2)
substract_operator = substract(4, 2)
multiply_operator = multiply(4, 2)
division_operator = divide(4, 2)

print(add_operator)
print(substract_operator)
print(multiply_operator)
print(division_operator)