import sys

if len(sys.argv) < 2:
    print("Usage: Python exec.py <arg1> <arg2> <arg3> ..")
else:
    print(" ".join(sys.argv[1::]).swapcase()[::-1])
