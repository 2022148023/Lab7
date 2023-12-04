class not2DError(Exception):
    # Error for 1D list
    def __str__(self):
        return "[ERROR]: list is not 2D."


class unevenListError(Exception):
    # Error for uneven list
    def __str__(self):
        return "[ERROR]: inner lists are not same in length."


class improperMatrixError(Exception):
    # Error for incompatible matmul pair
    def __str__(self):
        return "[ERROR]: [a][b]*[c][d] not b==c."


def mul1d(arr1, arr2):
    # arr1 * arr2
    # [1,2,3] * [4,5,6]
    # return  1*4 + 2*5 + 3*6
    sum = 0
    for i in range(len(arr1)):
        sum += arr1[i] * arr2[i]
    return sum


class list_D2(list):
    def __init__(self, arr):
        # checks that all children of the array are arrays
        if not all(isinstance(sublist, list) for sublist in arr) or not len(arr) > 1:
            raise not2DError()
        # checks that all sublists are of same size, a set cannot have duplicate elements so all lengths must be same
        if len(set(len(sublist) for sublist in arr)) != 1:
            raise unevenListError()

        # store dimensions
        self.dimensions = (len(arr), len(arr[0]))

        self.extend(arr)

    def __str__(self):
        return f"list_2D: {self.dimensions[0]}*{self.dimensions[1]}"

    def transpose(self):
        # inialize empty array with proper dimensions for transpose
        list_transpose = [
            [0 for j in range(self.dimensions[0])] for i in range(self.dimensions[1])
        ]
        # loop through matrix
        for row in range(self.dimensions[0]):
            for col in range(self.dimensions[1]):
                # assign element
                list_transpose[col][row] = self[row][col]
        # return new instance of the transpose
        return list_D2(list_transpose)

    def __matmul__(self, others):
        # make sure multiplication is possible
        if self.dimensions[1] != others.dimensions[0]:
            raise improperMatrixError()

        # get transpose of the other matrix
        arr2_T = others.transpose()

        # initialize an empty list for the product
        product = [
            [0 for _ in range(others.dimensions[1])] for _ in range(self.dimensions[0])
        ]

        # multiply matrices accordingly
        for i in range(len(product)):
            for j in range(len(product[0])):
                product[i][j] = mul1d(self[i], arr2_T[j])

        # return new instance of the multiplication product
        list_product = list_D2(product)
        return list_product

    def avg(self):
        arr_sum = 0
        for arr in self:
            arr_sum += sum(arr)
        return arr_sum / (self.dimensions[0] * self.dimensions[1])
