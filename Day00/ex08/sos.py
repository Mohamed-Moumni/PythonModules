import sys

decode = {'A': '.-',
          'B': '-...',
          'C': '-.-.',
          'D': '-..',
          'E': '.',
          'F': '..-.',
          'G': '--.',
          'H': '....',
          'I': '..',
          'J': '.---',
          'K': '-.-',
          'L': '.-..',
          'M': '--',
          'N': '-.',
          'O': '---',
          'P': '.--.',
          'Q': '--.-',
          'R': '.-.',
          'S': '...',
          'T': '-',
          'U': '..-',
          'V': '...-',
          'W': '.--',
          'X': '-..-',
          'Y': '-.--',
          'Z': '--..',
          '1': '.----',
          '2': '..---',
          '3': '...--',
          '4': '....-',
          '5': '.....',
          '6': '-....',
          '7': '--...',
          '8': '---..',
          '9': '----.',
          '0': '-----',
          ' ': '/'}


check = True

if len(sys.argv) < 2:
    print("Usage: python sos.py <arg> <arg> <arg> ....")
else:
    args = " ".join(sys.argv[1::])
    for c in args:
        if c != ' ' and not (c.upper()).isalnum():
            check = False
            print("ERROR")
            break
    if check:
        for c in args:
            print(f"{decode[c.upper()]} ", end="")
