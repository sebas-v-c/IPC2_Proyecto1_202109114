from typing import Optional
from .node import MatrixNode, Node


class LinkedMatrix:
    def __init__(self, rows: int, columns: int) -> None:
        self.head: MatrixNode = MatrixNode(0, 0)
        if rows > 10000 or columns > 10000 or rows < 1 or columns < 1:
            raise Exception

        self.rows = rows
        self.columns = columns
        self.__create_matrix__(rows, columns)

    def __create_matrix__(self, rows: int, columns: int) -> None:
        left_node: MatrixNode = self.head
        first_column_node: MatrixNode = self.head
        for row in range(rows):
            for column in range(1, columns):
                # print(f"({left_node.row},{left_node.column})", end=" ")
                new_node = MatrixNode(row, column)
                left_node.right = new_node
                new_node.left = left_node
                left_node = new_node
                if row == 0:
                    continue
                up_node: MatrixNode = self.get_node(row - 1, column)
                up_node.down = new_node
                new_node.up = up_node

            # print(f"({left_node.row},{left_node.column})", end=" ")
            # print("")
            if row == rows - 1:
                continue
            new_node = MatrixNode(row + 1, 0)
            first_column_node.down = new_node
            new_node.up = first_column_node
            first_column_node = new_node
            left_node = new_node
            # print("//////")
            # print("Nuevo Nodo: ", new_node.row, new_node.column)

    def get_node(self, target_row: int, target_column: int) -> MatrixNode:
        current_node: MatrixNode = self.head
        for i in range(target_column):
            current_node = current_node.right
        for i in range(target_row):
            current_node = current_node.down

        return current_node

    def display_matrix(self) -> None:
        for row in range(self.rows):
            for column in range(self.columns):
                print(self.get_node(row, column).data, end=" ")
            print("")


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.__length__: int = 0

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def preppend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node
            current_node = current_node.next

    def __reversed__(self):
        current_node = self.tail
        while current_node is not None:
            yield current_node
            current_node = current_node.prev

    def __len__(self):
        return self.__length__
