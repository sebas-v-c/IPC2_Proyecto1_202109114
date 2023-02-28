from typing import Optional
from .node import MatrixNode, Node


class LinkedMatrix:
    def __init__(self, rows: int, columns: int) -> None:
        self.head: MatrixNode = MatrixNode(0, 0)
        if rows > 10000 or columns > 10000 or rows < 1 or columns < 1:
            raise Exception

        self.rows = rows
        self.columns = columns
        self._create_matrix(rows, columns)

    def _create_matrix(self, rows: int, columns: int) -> None:
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

    def display_matrix(self, size=1) -> None:
        for row in range(self.rows):
            for column in range(self.columns):
                if self.get_node(row, column) is None:
                    print(" " * size, end=" ")
                print(self.get_node(row, column).data, end=" ")
            print("")


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.__length: int = 0

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def preppend(self, data) -> None:
        self.__length += 1
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def append(self, data) -> None:
        self.__length += 1
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def remove_node(self, node: Node) -> None:
        if self.__length == 0:
            raise IndexError

        if node is self.head:
            self.__length -= 1
            self.head = self.head.next
            self.head.prev = None
            return
        elif node is self.tail:
            self.__length -= 1
            self.tail = self.tail.prev
            self.tail.next = None
            return

        current_node = self.head.next
        while current_node is not None:
            if current_node is node:
                current_node.next.prev = current_node.prev
                current_node.prev.next = current_node.next
                self.__length -= 1
                return
            current_node = current_node.next

        raise KeyError

    def __getitem__(self, index: int):
        if index > self.__length or index < 0:
            raise IndexError
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        return current_node

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next

    def __reversed__(self):
        current_node = self.tail
        while current_node is not None:
            yield current_node.data
            current_node = current_node.prev

    def __len__(self):
        return self.__length
