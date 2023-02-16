from typing import List
from typing import Tuple


class Vector:
    def __init__(self,values:List[List[float]], shape:Tuple(int,int)):
        self.values = values
        self.shape = shape
    def dot(self, vect):
        if not isinstance(vect, Vector):
            print(f"The vect arg is not a Vector object")
            return
        if self.shape != vect.shape:
            print(f"The shape of the vectors is diffrent you cannot perform multiplication")
            return
        product = Vector()
        for v1, v2 in zip(self.values[0], vect.values[0]):
            product.values[0].append(v1 * v2)
        return product

a = Vector([[1.0, 2.0, 3.0]], (1,3))

b = Vector([[2.0, 2.0, 2.0]], (1,3))

c = a.dot(b)

print(c.values)
