from os import execve
from typing import Optional

from linkedList.linkedList import LinkedList, LinkedMatrix
from linkedList.node import MatrixNode
from samples.organism import Organism
import copy


class Sample:
    def __init__(
        self, sample_code: str, sample_desciption: str, rows: int, columns: int
    ) -> None:
        self.sample_code: str = sample_code
        self.sample_description: str = sample_desciption
        self.organisms: LinkedList = LinkedList()

        self.test_grid: LinkedMatrix = LinkedMatrix(rows, columns)

    def place_living_cell(self, organism: str, row: int, column: int) -> None:
        self.test_grid.get_node(row, column).data = organism

    def get_grid_dimentions(self) -> tuple[int, int]:
        return (self.test_grid.rows, self.test_grid.columns)

    def get_cell(self, target_row: int, target_column: int) -> MatrixNode:
        return self.test_grid.get_node(target_row, target_column)

    def copy_test_grid(self) -> LinkedMatrix:
        rows, columns = self.get_grid_dimentions()
        new_matrix = LinkedMatrix(rows, columns)
        for row in range(rows):
            for column in range(columns):
                current_node = self.get_cell(row, column)
                if current_node.data is not None:
                    new_matrix.get_node(row, column).data = copy.deepcopy(
                        current_node.data
                    )
        return new_matrix

    def simulate_sample_at_cell(
        self, row: int, column: int, organism_code: str
    ) -> bool:
        target_node: MatrixNode = self.get_cell(row, column)
        life_suitable = False
        if self._life_suitable_in_direction("UP", target_node):
            life_suitable = True
            next_node = target_node.up
            while next_node is not None and next_node.data is not None:
                next_node.data = organism_code
                next_node = target_node.up
        elif self._life_suitable_in_direction("DOWN", target_node):
            life_suitable = True
            next_node = target_node.down
            while next_node is not None and next_node.data is not None:
                next_node.data = organism_code
                next_node = target_node.down
        elif self._life_suitable_in_direction("RIGHT", target_node):
            life_suitable = True
            next_node = target_node.right
            while next_node is not None and next_node.data is not None:
                next_node.data = organism_code
                next_node = target_node.right
        elif self._life_suitable_in_direction("LEFT", target_node):
            life_suitable = True
            next_node = target_node.left
            while next_node is not None and next_node.data is not None:
                next_node.data = organism_code
                next_node = target_node.left
        elif self._life_suitable_in_direction("UP_RIGHT", target_node):
            print("HOLA")
            life_suitable = True
            next_node = target_node.up.right
            while next_node is not None and next_node.data is not None:
                next_node.data = organism_code
                next_node = self._get_diagonal_node("up", "right", target_node)
        elif self._life_suitable_in_direction("UP_LEFT", target_node):
            life_suitable = True
            next_node = target_node.up.left
            while next_node is not None and next_node.data is not None:
                next_node.data = organism_code
                next_node = self._get_diagonal_node("up", "left", target_node)
        elif self._life_suitable_in_direction("DOWN_RIGHT", target_node):
            life_suitable = True
            next_node = target_node.down.right
            while next_node is not None and next_node.data is not None:
                next_node.data = organism_code
                next_node = self._get_diagonal_node("down", "right", target_node)
        elif self._life_suitable_in_direction("DOWN_LEFT", target_node):
            life_suitable = True
            next_node = target_node.down.left
            while next_node is not None and next_node.data is not None:
                next_node.data = organism_code
                next_node = self._get_diagonal_node("down", "left", target_node)

        return life_suitable

    def _life_suitable_in_direction(self, dir: str, organism_node: MatrixNode) -> bool:
        life_suitable = False
        life_form_change = False
        if dir == "UP":
            print("UP")
            next_node = organism_node
            while next_node is not None and next_node.data is not None:
                next_node = organism_node.up
                if life_form_change and next_node.data == organism_node.data:
                    life_suitable = True
                    break
                elif next_node.data == organism_node.data:
                    next_node = organism_node.up
                    continue
                life_form_change = True

        elif dir == "DOWN":
            print("DOWN")
            print(organism_node.row, organism_node.column)
            next_node = organism_node
            while next_node is not None and next_node.data is not None:
                next_node = organism_node.down
                if life_form_change and next_node.data == organism_node.data:
                    life_suitable = True
                    break
                elif next_node.data == organism_node.data:
                    continue
                print(next_node.data)
                life_form_change = True
        elif dir == "RIGHT":
            print("RIGHT")
            next_node = organism_node
            while next_node is not None and next_node.data is not None:
                next_node = organism_node.right
                if life_form_change and next_node.data == organism_node.data:
                    life_suitable = True
                    break
                elif next_node.data == organism_node.data:
                    continue
                life_form_change = True
        elif dir == "LEFT":
            print("LEFT")
            next_node = organism_node
            while next_node is not None and next_node.data is not None:
                next_node = organism_node.left
                if life_form_change and next_node.data == organism_node.data:
                    life_suitable = True
                    break
                elif next_node.data == organism_node.data:
                    continue
                life_form_change = True
        elif dir == "UP_RIGHT":
            print("UP_RIGHT")
            next_node = organism_node
            while next_node is not None and next_node.data is not None:
                next_node = self._get_diagonal_node("up", "right", organism_node)
                if life_form_change and next_node.data == organism_node.data:
                    life_suitable = True
                    break
                elif next_node.data == organism_node.data:
                    continue
                life_form_change = True
        elif dir == "UP_LEFT":
            print("UP_LEFT")
            # print(organism_node.row, organism_node.column)
            # print(next_node.row, next_node.column)
            next_node = organism_node
            while next_node is not None and next_node.data is not None:
                next_node = self._get_diagonal_node("up", "left", organism_node)
                if life_form_change and next_node.data == organism_node.data:
                    life_suitable = True
                    break
                elif next_node.data == organism_node.data:
                    continue
                life_form_change = True
        elif dir == "DOWN_RIGHT":
            print("DOWN_RIGHT")
            # print(organism_node.row, organism_node.column)
            # print(next_node.row, next_node.column)
            next_node = organism_node
            while next_node is not None and next_node.data is not None:
                next_node = self._get_diagonal_node("down", "right", organism_node)
                print(next_node.data)
                if life_form_change and next_node.data == organism_node.data:
                    life_suitable = True
                    break
                elif next_node.data == organism_node.data:
                    continue
                life_form_change = True
        elif dir == "DOWN_LEFT":
            print("DOWN_LEFT")
            next_node = organism_node
            while next_node is not None and next_node.data is not None:
                next_node = self._get_diagonal_node("down", "left", organism_node)
                if life_form_change and next_node.data == organism_node.data:
                    life_suitable = True
                    break
                elif next_node.data == organism_node.data:
                    continue
                life_form_change = True

        return life_suitable

    def _get_diagonal_node(
        self, up_down: str, left_right: str, current_node: MatrixNode
    ) -> Optional[MatrixNode]:
        try:
            return getattr(getattr(current_node, up_down), left_right)
        except:
            return None

    def can_live_at(self, row: int, column: int, roganism_code: str) -> bool:
        return True

    def get_head_node(self) -> MatrixNode:
        return self.test_grid.head
