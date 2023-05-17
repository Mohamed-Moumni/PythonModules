from vector import Vector

try:
    v3 = Vector([[1.0, 3.0]])
    v4 = Vector([[2.0, 4.0]])
    # print(v3.values)
    # print(v4.values)
    # v5 = v3 - v4
    # v6 = v4 - v3
    # print(v5.values)
    # print(v6.values)
    2.0 * v3
    print(v3)
except (ZeroDivisionError, NotImplementedError) as msg:
    print(msg)

# print(v5.values)