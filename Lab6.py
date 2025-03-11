def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def modular_inverse(a, b):
    gcd, x, y = gcd_extended(a, b)
    if gcd != 1:
        return None
    return x % b

a = 17
b = 23

inverse = modular_inverse(a, b)

if inverse is None:
    print("Modular inverse does not exist.")
else:
    print(f"Modular inverse of {a} modulo {b} is: {inverse}")
