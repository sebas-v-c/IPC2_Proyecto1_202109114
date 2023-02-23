from .node import MatrixNode


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
