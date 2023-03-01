from typing import List

class Vector:
    """class to represent a vector in mathematics format"""

    def __init__(self, Values):

        if isinstance(Values, int):
            self.shape = (Values, 1)
            self.values = list()
            self.values.append(list(range(Values)))
        elif isinstance(Values, tuple):
            if len(Values) > 2 or Values[0] > Values[1]:
                print("Construct Your object with tuple of two integer (a,b) with a < b")
                return
            else:
                Values_ = list(range(Values[0],Values[1]))
                self.values = list()
                for i in Values_:
                    temp = []
                    temp.append(i)
                    self.values.append(temp)
                self.shape = ((Values[1] - Values[0]), 1)
        elif isinstance(Values, list):
            ret = self.is_vector(Values)
            if ret == -1:
                print("That is not a representation of vector")
                return
            elif ret == 1:
                self.shape = (1, len(Values[0]))
                self.values = Values
            else:
                self.shape = (len(Values), 1)
                self.values = Values
        else:
            print("you can't construct an object from your input")
            return

    def is_vector(self, Values) -> int:
        """This function return true if the given list is a vector"""
        if len(Values) == 1:
            if all([isinstance(item, float) for item in Values[0]]):
                return 1
            return -1
        else:
            if all([isinstance(item,list) and len(item) == 1 and isinstance(item[0], float) for item in Values]):
                return 2
            return -1

    def T(self):
        """This function return the Transpoe of vector"""
        trans = []
        if self.shape[0] == 1:
            for i in range(self.shape[1]):
                trans.append([self.values[0][i]])
            Trans_vector = Vector(trans)
            Trans_vector.shape = (self.shape[1], self.shape[0])
            return Trans_vector
        else:
            for i in range(self.shape[0]):
                trans.append(self.values[i][0])
            Trans_vector = Vector(trans)
            Trans_vector.shape = (self.shape[1], self.shape[0])
            return Trans_vector

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

    def __add__(self, other):
        if isinstance(other, Vector):
            if self.shape != other.shape:
                print("You can't do an addition operation on two vector that have different dimension")
                return
            else:
                addition = []
                if self.shape[0] == 1:
                    for i in range(self.shape[1]):
                        addition.append(self.values[0][i] + other.values[0][i])
                    return Vector([addition])
                else:
                    for i in range(self.shape[0]):
                        addition.append([self.values[i][0] + other.values[i][0]])
                    return Vector(addition)
        else:
            print("Invalid Represenation of vector")
    
    def __radd__(self, other):
        if isinstance(other, Vector):
            if self.shape != other.shape:
                print("You can't do an addition operation on two vector that have different dimension")
                return
            else:
                addition = []
                if self.shape[0] == 1:
                    for i in range(self.shape[1]):
                        addition.append(self.values[0][i] + other.values[0][i])
                    return Vector([addition])
                else:
                    for i in range(self.shape[0]):
                        addition.append([self.values[i][0] + other.values[i][0]])
                    return Vector(addition)
        else:
            print("Invalid Represenation of vector")
    
    def __sub__(self, other):
        """this class method substruct two object of Vector of the same shape return Error"""
    
        if isinstance(other, Vector):
            if self.shape != other.shape:
                print("You can't do an addition operation on two vector that have different dimension")
                return
            else:
                substruction = []
                if self.shape[0] == 1:
                    for i in range(self.shape[1]):
                        substruction.append(other.values[0][i] - self.values[0][i])
                    return Vector([substruction])
                else:
                    for i in range(self.shape[0]):
                        substruction.append([other.values[i][0]] - self.values[i][0])
                    return Vector(substruction)
        else:
            print("Invalid Represenation of vector")
    
    def __rsub__(self, other):
        """this class method substruct two object of Vector of the same shape return Error"""
    
        if isinstance(other, Vector):
            if self.shape != other.shape:
                print("You can't do an addition operation on two vector that have different dimension")
                return
            else:
                substruction = []
                if self.shape[0] == 1:
                    for i in range(self.shape[1]):
                        substruction.append(other.values[0][i] - self.values[0][i])
                    return Vector([substruction])
                else:
                    for i in range(self.shape[0]):
                        substruction.append([other.values[i][0]] - self.values[i][0])
                    return Vector(substruction)
        else:
            print("Invalid Represenation of vector")
    
    def __truediv__(self, scalar):
        if not isinstance(scalar, float):
            print("division is only by scalar")
            return
        if scalar == 0:
            print("ZerodivisionError: division by zero.")
        else:
            if self.shape[0] == 1:
                for i in range(self.shape[1]):
                    self.values[0][i] /= scalar
            else:
                for i in range(self.shape[0]):
                    self.values[i][0] /= scalar

    def __rtruediv__(self, scalar):
        print("Division of a scalar by a Vector is not defined here.")
        return 

    
    def __mul__(self, scalar):
        """"""

        if not isinstance(scalar, float):
            print("multiplication is only by scalar")
        else:
            if self.shape[0] == 1:
                for i in range(self.shape[1]):
                    self.values[0][i] *= scalar
            else:
                for i in range(self.shape[0]):
                    self.values[i][0] *= scalar

    def __rmul__(self, scalar) -> None:
        """"""

        if not isinstance(scalar, float):
            print("multiplication is only by scalar")
        else:
            if self.shape[0] == 1:
                for i in range(self.shape[1]):
                    self.values[0][i] *= scalar
            else:
                for i in range(self.shape[0]):
                    self.values[i][0] *= scalar
    
    def __str__(self) -> str:
        return f"{self.values}"

    def __repr__(self) -> str:
        return f"{self.values}"