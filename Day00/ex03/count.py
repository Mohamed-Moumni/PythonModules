import string
import sys


def text_analyzer(data=None):
    """This function counts the number of upper characters,\
        lower characters, punctuation and spaces in a given text."""
    if (data is None):
        data = input("Enter a text To analyzing it")
    if type(data) is not str:
        print("Arguments is not a string")
    else:
        print(f"The text contains {len(data)} character(s)")
        print(f"- {sum(1 for c in data if c.isupper())} upper letter(s)")
        print(f"- {sum(1 for c in data if c.islower())} lower letter(s)")
        print(f"- {sum(1 for c in data if c in string.punctuation)}\
 punctuation letter(s)")
        print(f"- {sum(1 for c in data if c.isspace())} space letter(s)")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        print("AssertionError: Invalid number of Argument provided")
