from random import random

def generator(text, sep=" ", option=None):
    """Splits the text according to sep value and yield the substrings. 
    option precise if a action is performed to the substrings before it is yielded."""
    if not isinstance(text, str):
        print("ERROR")
        return None
    splited = text.split(sep)
    options = ["shuffle", "unique", "ordered", None]
    if not option in options:
        print("ERROR")
    else:
        if option != None:
            if option == "shuffle":
                splited = sorted(splited,key=lambda x: random())
            elif option == "unique":
                splited = list(set(splited))
            elif option == "ordered":
                splited.sort()
        for word in splited:
            yield word