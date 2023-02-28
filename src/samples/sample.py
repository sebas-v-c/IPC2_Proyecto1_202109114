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

    def simulate_sample_at(self, row: int, column: int, organism_code: str) -> bool:
        """Simulate the sample and if is suitable for life don't change nothing in the sample"""
        target_node: MatrixNode = self.get_cell(row, column)
        if target_node.data is not None:
            raise ValueError
        target_node.data = organism_code
        suitable_for_life = False
        if self._life_suitable_in_direction("UP", target_node):
            suitable_for_life = True
        elif self._life_suitable_in_direction("DOWN", target_node):
            suitable_for_life = True
        elif self._life_suitable_in_direction("RIGHT", target_node):
            suitable_for_life = True
        elif self._life_suitable_in_direction("LEFT", target_node):
            suitable_for_life = True
        elif self._life_suitable_in_direction("UP_RIGHT", target_node):
            suitable_for_life = True
        elif self._life_suitable_in_direction("UP_LEFT", target_node):
            suitable_for_life = True
        elif self._life_suitable_in_direction("DOWN_RIGHT", target_node):
            suitable_for_life = True
        elif self._life_suitable_in_direction("DOWN_LEFT", target_node):
            suitable_for_life = True

        target_node.data = None
        return suitable_for_life

    def simulate_sample_at_cell(
        self, row: int, column: int, organism_code: str
    ) -> bool:
        """Simulate the sample and if is suitable for life change the values"""
        target_node: MatrixNode = self.get_cell(row, column)
        if target_node.data is not None:
            raise ValueError
        target_node.data = organism_code
        suitable_for_life = False
        if self._life_suitable_in_direction("UP", target_node):
            suitable_for_life = True
            next_node = target_node.up
            while next_node is not None and next_node.data is not None:
                next_node.data = organism_code
                next_node = next_node.up
        elif self._life_suitable_in_direction("DOWN", target_node):
            suitable_for_life = True
            next_node = target_node.down
            while next_node is not None and next_node.data is not None:
                next_node.data = organism_code
                next_node = next_node.down
        elif self._life_suitable_in_direction("RIGHT", target_node):
            suitable_for_life = True
            next_node = target_node.right
            while next_node is not None and next_node.data is not None:
                next_node.data = organism_code
                next_node = next_node.right
        elif self._life_suitable_in_direction("LEFT", target_node):
            suitable_for_life = True
            next_node = target_node.left
            while next_node is not None and next_node.data is not None:
                next_node.data = organism_code
                next_node = next_node.left
        elif self._life_suitable_in_direction("UP_RIGHT", target_node):
            suitable_for_life = True
            next_node = target_node.up.right
            while next_node is not None and next_node.data is not None:
                next_node.data = organism_code
                next_node = self._get_diagonal_node("up", "right", next_node)
        elif self._life_suitable_in_direction("UP_LEFT", target_node):
            suitable_for_life = True
            next_node = target_node.up.left
            while next_node is not None and next_node.data is not None:
                next_node.data = organism_code
                next_node = self._get_diagonal_node("up", "left", next_node)
        elif self._life_suitable_in_direction("DOWN_RIGHT", target_node):
            suitable_for_life = True
            next_node = target_node.down.right
            while next_node is not None and next_node.data is not None:
                next_node.data = organism_code
                next_node = self._get_diagonal_node("down", "right", next_node)
        elif self._life_suitable_in_direction("DOWN_LEFT", target_node):
            suitable_for_life = True
            next_node = target_node.down.left
            while next_node is not None and next_node.data is not None:
                next_node.data = organism_code
                next_node = self._get_diagonal_node("down", "left", next_node)

        if not suitable_for_life:
            target_node.data = None
        return suitable_for_life

    def _life_suitable_in_direction(self, dir: str, target_node: MatrixNode) -> bool:
        life_suitable = False
        life_form_change = False
        if dir == "UP":
            next_node = target_node
            while next_node is not None and next_node.data is not None:
                if life_form_change and next_node.data == target_node.data:
                    life_suitable = True
                    break
                elif next_node.data == target_node.data:
                    next_node = next_node.up
                    continue
                next_node = next_node.up
                life_form_change = True

        elif dir == "DOWN":
            next_node = target_node
            while next_node is not None and next_node.data is not None:
                if life_form_change and next_node.data == target_node.data:
                    life_suitable = True
                    break
                elif next_node.data == target_node.data:
                    next_node = next_node.down
                    continue
                next_node = next_node.down
                life_form_change = True
        elif dir == "RIGHT":
            next_node = target_node
            while next_node is not None and next_node.data is not None:
                if life_form_change and next_node.data == target_node.data:
                    life_suitable = True
                    break
                elif next_node.data == target_node.data:
                    next_node = next_node.right
                    continue
                next_node = next_node.right
                life_form_change = True
        elif dir == "LEFT":
            next_node = target_node
            while next_node is not None and next_node.data is not None:
                if life_form_change and next_node.data == target_node.data:
                    life_suitable = True
                    break
                elif next_node.data == target_node.data:
                    next_node = next_node.left
                    continue
                next_node = next_node.left
                life_form_change = True
        elif dir == "UP_RIGHT":
            next_node = target_node
            while next_node is not None and next_node.data is not None:
                if life_form_change and next_node.data == target_node.data:
                    life_suitable = True
                    break
                elif next_node.data == target_node.data:
                    next_node = self._get_diagonal_node("up", "right", next_node)
                    continue
                next_node = self._get_diagonal_node("up", "right", next_node)
                life_form_change = True
        elif dir == "UP_LEFT":
            # print(organism_node.row, organism_node.column)
            # print(next_node.row, next_node.column)
            next_node = target_node
            while next_node is not None and next_node.data is not None:
                if life_form_change and next_node.data == target_node.data:
                    life_suitable = True
                    break
                elif next_node.data == target_node.data:
                    next_node = self._get_diagonal_node("up", "left", next_node)
                    continue
                next_node = self._get_diagonal_node("up", "left", next_node)
                life_form_change = True
        elif dir == "DOWN_RIGHT":
            # print(organism_node.row, organism_node.column)
            # print(next_node.row, next_node.column)
            next_node = target_node
            while next_node is not None and next_node.data is not None:
                if life_form_change and next_node.data == target_node.data:
                    life_suitable = True
                    break
                elif next_node.data == target_node.data:
                    next_node = self._get_diagonal_node("down", "right", next_node)
                    continue
                next_node = self._get_diagonal_node("down", "right", next_node)
                life_form_change = True
        elif dir == "DOWN_LEFT":
            next_node = target_node
            while next_node is not None and next_node.data is not None:
                if life_form_change and next_node.data == target_node.data:
                    life_suitable = True
                    break
                elif next_node.data == target_node.data:
                    next_node = self._get_diagonal_node("down", "left", next_node)
                    continue
                next_node = self._get_diagonal_node("down", "left", next_node)
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
