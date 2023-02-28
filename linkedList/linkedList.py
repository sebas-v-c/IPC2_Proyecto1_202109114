from .node import MatrixNode


class LinkedMatrix:
    def __init__(self, rows: int, columns: int) -> None:
        self.head: MatrixNode = MatrixNode(0, 0)
        self.rows = rows
        self.columns = columns
        __create_matrix(rows, columns)

    def __create_matrix(self, rows: int, columns: int) -> None:
        pass

    def insert(self, new_node):
        if self.head:
            last_node = self.head
            while last_node.next != None:
                last_node = last_node.next

            new_node.prev = last_node
            last_node.next = new_node

        else:
            self.head = new_node

    def display(self):
        print("Normal Order: ", end="")

        temp_node = self.head
        while temp_node != None:
            print(temp_node.data, end=" ")
            temp_node = temp_node.next
        print()

        print("Reverse Order: ", end="")

        last_node = self.head
        while last_node.next != None:
            last_node = last_node.next

        temp_node = last_node
        while temp_node != None:
            print(temp_node.data, end=" ")
            temp_node = temp_node.prev
        print()
