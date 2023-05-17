import typing
# Todo
#1. Create constructors Good
#2. Create dot and T member function
#3. Operations in vectors
#4. Create magic/special methods

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
