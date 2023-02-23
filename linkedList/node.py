class MatrixNode:
    def __init__(self, row: int, column: int) -> None:
        self.row: int = row
        self.column: int = column
        self._data = 0
        self._left = None
        self._right = None
        self._up = None
        self._down = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left: "MatrixNode"):
        self._left: MatrixNode = left

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right: "MatrixNode"):
        self._right: MatrixNode = right

    @property
    def up(self):
        return self._up

    @up.setter
    def up(self, up: "MatrixNode"):
        self._up: MatrixNode = up

    @property
    def down(self):
        return self._down

    @down.setter
    def down(self, down: "MatrixNode"):
        self._down: MatrixNode = down