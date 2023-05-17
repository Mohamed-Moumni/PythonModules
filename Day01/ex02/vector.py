import typing

class Vector:
    def __init__(self, vect) -> None:
        if isinstance(vect, int):
            self.shape = (vect, 1)
            self.values = [float(i) for i in range(vect)]
        elif isinstance(vect, tuple) and len(vect) == 2:
            self.shape = (len(vect), 1)
            self.values = [float(i) for i in range(vect[0], vect[1])]
        elif isinstance(vect, list) and isinstance(vect[0], list) and len(vect) > 0:
            if len(vect) != 1:
                if not all((isinstance(item, list) and len(item) == 1 for item in vect)):
                    raise TypeError("Invalid Type Error")
                for i in range(len(vect)):
                    if not isinstance(vect[i][0], float):
                        raise TypeError("Invalid Type Error")
                self.shape = (len(vect), 1)
            else:
                for i in range(len(vect[0])):
                    if not isinstance(vect[0][i], float):
                        raise TypeError("Invalid Type Error")
                self.shape = (1, len(vect[0]))
            self.values = vect
        else:
            raise TypeError("Invalid Type Error")

    def dot(self, vector):
        if not isinstance(vector, Vector):
            print("Error: The value is not a vector")
        elif self.shape[0] != vector.shape[0] or self.shape[1] != vector.shape[1]:
            print("Error: The shape of two vectors is different")
        else:
            dot_product = 0
            if vector.shape[0] != 1:
                for i in range(vector.shape[0]):
                    dot_product += self.values[i][0] * vector.values[i][0]
            else:
                for i in range(vector.shape[1]):
                    dot_product += self.values[0][i] * vector.values[0][i]
            return (dot_product)
    
    def T(self) -> None:
        if not isinstance(self, Vector):
            print("Error: The value is not a vector")
        else:
            size = self.shape[0] if self.shape[0] != 1 else self.shape[1]
            newVect = []
            if self.shape[0] != 1:
                self.shape = (1, size)
                for i in range(size):
                    newVect.append(self.values[i][0])
            else:
                self.shape = (size, 1)
                for i in range(size):
                    newVect.append([self.values[0][i]])
            self.values = newVect
    
    def __add__(self, other):
        if not isinstance(self, Vector) or not isinstance(other, Vector):
            print("Error: The value is not a vector")
            return None
        elif self.shape[0] != other.shape[0] or self.shape[1] != other.shape[1]:
            print("Error: The shape of two vectors is different")
            return None
        else:
            sum = []
            if self.shape[0] != 1:
                for i in range(self.shape[0]):
                    sum.append([self.values[i][0] + other.values[i][0]])
            else:
                for i in range(self.shape[1]):
                    sum.append(self.values[0][i] + other.values[0][i])
            return Vector([sum])
    
    def __radd__(self, other):
        if not isinstance(self, Vector) or not isinstance(other, Vector):
            print("Error: The value is not a vector")
            return None
        elif self.shape[0] != other.shape[0] or self.shape[1] != other.shape[1]:
            print("Error: The shape of two vectors is different")
            return None
        else:
            sum = []
            if self.shape[0] != 1:
                for i in range(self.shape[0]):
                    sum.append([self.values[i][0] + other.values[i][0]])
            else:
                for i in range(self.shape[1]):
                    sum.append(self.values[0][i] + other.values[0][i])
            return Vector([sum])
    
    def __sub__(self, other):
        if not isinstance(self, Vector) or not isinstance(other, Vector):
            print("Error: The value is not a vector")
            return None
        elif self.shape[0] != other.shape[0] or self.shape[1] != other.shape[1]:
            print("Error: The shape of two vectors is different")
            return None
        else:
            sub = []
            if self.shape[0] != 1:
                for i in range(self.shape[0]):
                    sub.append([self.values[i][0] - other.values[i][0]])
            else:
                for i in range(self.shape[1]):
                    sub.append(self.values[0][i] - other.values[0][i])
            return Vector([sub])
    
    def __rsub__(self, other):
        if not isinstance(self, Vector) or not isinstance(other, Vector):
            print("Error: The value is not a vector")
            return None
        elif self.shape[0] != other.shape[0] or self.shape[1] != other.shape[1]:
            print("Error: The shape of two vectors is different")
            return None
        else:
            sub = []
            if self.shape[0] != 1:
                for i in range(self.shape[0]):
                    sub.append([self.values[i][0] - other.values[i][0]])
            else:
                for i in range(self.shape[1]):
                    sub.append(self.values[0][i] - other.values[0][i])
            return Vector([sub])

    def __truediv__(self, divider) -> None:
        if not isinstance(self, Vector) or not isinstance(divider, float):
            print("Error: The divider value is not a float")
        elif divider == 0.0:
            raise ZeroDivisionError("division by zero.")
        else:
            if self.shape[0] != 1:
                for i in range(self.shape[0]):
                    self.values[i][0] /= divider
            else:
                for i in range(self.shape[1]):
                    self.values[0][i] /= divider

    def __rtruediv__(self, divider) -> None:
        raise NotImplementedError("Division of a scalar by a Vector is not defined here.")
    
    def __mul__(self, factor) -> None:
        if not isinstance(self, Vector) or not isinstance(factor, float):
            print("Error: The factor value is not a float")
        else:
            if self.shape[0] != 1:
                for i in range(self.shape[0]):
                    self.values[i][0] *= factor
            else:
                for i in range(self.shape[1]):
                    self.values[0][i] *= factor

    def __rmul__(self, factor) -> None:
        if not isinstance(self, Vector) or not isinstance(factor, float):
            print("Error: The factor value is not a float")
        else:
            if self.shape[0] != 1:
                for i in range(self.shape[0]):
                    self.values[i][0] *= factor
            else:
                for i in range(self.shape[1]):
                    self.values[0][i] *= factor

    def __str__(self) -> str:
        return str(self.values)

    def __repr__(self) -> str:
        return str(self.values)
