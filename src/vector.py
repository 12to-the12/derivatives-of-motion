# my beautiful vector class
class Vector:
    def __init__(self, vector: list):
        assert type(vector) == list, "no"
        self.vector: list = vector

    # the magnitude of a vector is the sqrt of the sum of the square of it's components
    @property
    def mag(self) -> float:
        s = sum([x**2 for x in self.vector])
        mag = (s) ** 0.5

        return mag

    @property
    def unit(self):
        return Vector([x / self.mag for x in self.vector])

    @property
    def len(self) -> int:
        return len(self.vector)

    def dot(self, other):
        return sum([x * y for x, y in zip(self.vector, other.vector)])

    def __str__(self) -> str:
        # out = ""
        # for index, item in enumerate(self.vector):
        #     out += f"#{index}: {item}"
        # return out
        return str(self.vector)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector([x + y for x, y in zip(self.vector, other.vector)])
        # elif isinstance(other, (int, float)):
        # 	# return Vector([x+other for x in self.vector])
        else:
            return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector([x * y for x, y in zip(self.vector, other.vector)])
        elif isinstance(other, (int, float)):
            return Vector([x * other for x in self.vector])
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __matmul__(self, other):
        if isinstance(other, Vector):
            return self.dot(other)
        else:
            return NotImplemented


# print(5)
# def xxx(): return 1+1
# def test_xxx():
#     assert round(Vector([1,1]).mag,2)==1.41,"wrong answer"
