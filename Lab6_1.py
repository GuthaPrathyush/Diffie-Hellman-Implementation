def add_large_numbers(a, b):
    return str(int(a) + int(b))

def subtract_large_numbers(a, b):
    return str(int(a) - int(b))

def multiply_large_numbers(a, b):
    return str(int(a) * int(b))

def divide_large_numbers(a, b):
    if b == "0":
        return "Undefined"
    return str(int(a) // int(b))

a = "987654321987654321987654321987654321"
b = "123456789123456789123456789123456789"

print("Addition:", add_large_numbers(a, b))
print("Subtraction:", subtract_large_numbers(a, b))
print("Multiplication:", multiply_large_numbers(a, b))
print("Division:", divide_large_numbers(a, b))
