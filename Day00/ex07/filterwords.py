import sys
import string

if len(sys.argv) != 3:
    print("ERROR: Invalid Number of arguments provided")
elif not isinstance(sys.argv[1], str):
    print("ERROR: The argument is not a string")
elif not sys.argv[2].isnumeric():
    print("ERROR: The argument is not an integer")
else:
    arg = sys.argv[1].split()
    N = int(sys.argv[2])
    result = []
    for elem in arg:
        for c in elem:
            if c in string.punctuation:
                elem = elem.replace(c, "")
        if len(elem) >= N:
            result.append(elem)
    print(result)
