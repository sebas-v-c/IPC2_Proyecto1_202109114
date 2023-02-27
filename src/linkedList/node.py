from typing import Optional


class MatrixNode:
    def __init__(self, row: int, column: int) -> None:
        self.row: int = row
        self.column: int = column
        self._data = None
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


class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self._next = None
        self._prev = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next: Optional["Node"]):
        self._next: Optional[Node] = next

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev: Optional["Node"]):
        self._prev: Optional[Node] = prev
