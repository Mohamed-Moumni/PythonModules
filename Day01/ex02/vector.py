from typing import List

class Vector:
    """class to represent a vector in mathematics format"""

    def __init__(self, Values):

        if isinstance(Values, int):
            iterable = list()
            iterable.append(list(range(Values)))
            self.shape = (Values, 1)
            self.values = iterable
        elif isinstance(Values, tuple):
            if len(Values) > 2 or Values[0] > Values[1]:
                print("Construct Your object with tuple of two integer (a,b) with a < b")
                return
            else:
                Values_ = list(range(Values[0],Values[1]))
                numbers = []
                for i in Values_:
                    temp = []
                    temp.append(i)
                    numbers.append(temp)
                self.values = numbers
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
            else:
                addition = []
                if self.shape[0] == 1:
                    for i in range(self.shape[1]):
                        addition.append(self.values[0][i] + other.values[0][i])
                
                return Vector([addition])
        else:
            print("Invalid Represenation of vector")
            
