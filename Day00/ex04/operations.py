import sys

if len(sys.argv) < 3:
    print("Usage: python operations.py <number1> <number2>")
elif len(sys.argv) > 3:
    print("AssertionError: too many arguments")
elif type(sys.argv[1]) == int or type(sys.argv[2]) == int:
    print("AssertionError: only integers")
else:
    number1 = int(sys.argv[1])
    number2 = int(sys.argv[2])
    print(f"Sum: {number1 + number2}")
    print(f"Difference: {number1 - number2}")
    print(f"Product: {number1 * number2}")
    if (number2 == 0):
        print(f"Quotient: ERROR (division by zero)")
        print(f"Remainer: ERROR (division by zero)")
    else:
        print(f"Quotient: {number1 / number2}")
        print(f"Remainder: {number1 % number2}")
