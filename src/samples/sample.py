from typing import Optional

from linkedList.linkedList import LinkedList, LinkedMatrix
from linkedList.node import MatrixNode
from samples.organism import Organism


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

    def simulate_sample_at(
        self, row: int, column: int, organism_code: str
    ) -> Optional["Sample"]:
        rows, columns = self.get_grid_dimentions()
        # TODO make this crazy shit happens
        return Sample(
            self.sample_code + "-" + organism_code,
            self.sample_description,
            rows,
            columns,
        )

    def get_head_node(self) -> MatrixNode:
        return self.test_grid.head
