from typing import List
from typing import Tuple
import operator


class Vector:
    def __init__(self,values:List[List[float]], shape:Tuple[int,int]):
        self.values = values
        self.shape = shape
    def dot(self, vect):
        if not isinstance(vect, Vector):
            print(f"The vect arg is not a Vector object")
            return
        if self.shape != vect.shape:
            print(f"The shape of the vectors is diffrent you cannot perform multiplication")
            return
        product = Vector([],(self.shape[0], self.shape[1]))
        for v1, v2 in zip(self.values, vect.values):
            product.values.append(v1 * v2)
        return product
    def T(self):
        if self.shape[0] == 1:
            trans = Vector([], (self.shape[1], self.shape[0]))
            for i in range(self.shape[1]):
                trans.values.append([self.values[i]])
            return trans
        else:
            trans = Vector([],(self.shape[1], self.shape[0]))
            for i in range(self.shape[0]):
                trans.values.append(self.values[i][0])
            return trans

vect1 = Vector([[1.0], [2.0], [3.0]], (3,1))

# vect2 = Vector([2.0, 2.0, 2.0], (3,1))

# vect2 = operator.mul(vect2, 5)

# vect3 = vect1.T()

# print(vect3.shape)

# vect3 = vect1.dot(vect2)

# print(vect3.values)