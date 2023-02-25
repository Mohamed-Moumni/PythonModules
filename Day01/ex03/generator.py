import random

def generator(text, sep=" ", option=None):
    """Splits the text according to sep value and yield the substrings.
        option precise if a action is performed to the substrings\
        before it is yielded.
    """

    if not isinstance(text, str):
        print("ERROR")
        exit(1)
    splited_text = text.split(sep)
    if option == "shuffle":
        random.shuffle(splited_text)
    elif option == "ordered":
        splited_text.sort()
    elif option == "unique":
        unique = []
        for elem in splited_text:
            if elem not in unique:
                unique.append(elem)
    else:
        print("ERROR")
        exit(1)
    splited_text.clear()
    splited_text = unique
    for elem in splited_text:
        yield elem
text = "Lorem Ipsum Lorem Ipsum"
for word in generator(text, sep=" ", option="unique"):
    print(word)
