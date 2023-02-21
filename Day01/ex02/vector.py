# import operator

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
        else:
            print("you can't construct an object from your input")
            return

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
        if self.shape != other.shape:
            print("You can't do an addition operation on two vector that have different dimension")
        else:
            addition = Vector(0)
            for i in range(len(self.values)):
                addition.values[i] = self.values[i] + other.values[i]
            return addition
















    # def isVector(self, Values) -> bool:
    #     for elem in Values:
    #         if not self.is_list(elem):
    #             return (False)
    #         else:
    #             for elem2 in elem:
    #                 if not self.is_list(elem2):
    #                     return (False)
    #     return (True)

# print(a.shape)
    # def is_list(self,values) -> bool:
    #     for elem in values:
    #         if isinstance(elem, list):
    #             return (False)
    #     return (True)

    # def get_shape(self,values:List[List[float]]) -> Tuple[int, int]:
    #     if isinstance(values[0], list):
    #         return (len(values), 1)
    #     return (1, len(values))

