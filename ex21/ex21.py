def add(a, b):
    print("ADDING: {} + {}".format(a, b))
    return a + b

def subtract(a, b):
    print("SUBTRACTING {} - {}".format(a, b))
    return a - b

def multiply(a, b):
    print("MULTIPLYING {} * {}".format(a, b))
    return a * b

def divide(a, b):
    print("DIVIDING {} / {}".format(a, b))
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: {}, Height: {}, Weight: {}, IQ: {}".format(age, height, weight, iq))


# A puzzle for the extra credit, type it in anyway
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
'''
divide(iq, 2) = divide(divide(100, 2), 2) = divide(50, 2) = 25
multiply(weight, 25) = multiply(multiply(90, 2), 25) = multiply(180, 25) = 4500
subtract(height, 4500) = subtract(subtract(78, 4), 4500) = subtract(74, 4500) = -4426
add(age, -4426) = add(add(30, 5), -4426) = add(35, -4426) = -4391
'''

print("That becomes: ", what, "Can you do it by hand?")

print("Me: Yep.")
