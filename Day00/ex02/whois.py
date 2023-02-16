import sys

if len(sys.argv) > 2:
    print("AssertionError: more than one argument are provided")
elif len(sys.argv) < 2:
    print("AssertionError: no Arguement is Provided")
elif not sys.argv[1].isnumeric():
    print("AssertionError: argument is not an integer")
else:
    number = int(sys.argv[1])
    if number == 0:
        print("I'm Zero.")
    elif number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
