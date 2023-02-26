from typing import Optional

from linkedList.linkedList import LinkedList, LinkedMatrix
from samples.organism import Organism


class Sample:
    def __init__(
        self, sample_code: str, sample_desciption: str, rows: int, columns: int
    ) -> None:
        self.sample_code: str = sample_code
        self.sample_description: str = sample_desciption
        self.organisms: LinkedList = LinkedList()

        self.__test_grid__: LinkedMatrix = LinkedMatrix(rows, columns)

    def place_living_cell(self, organism: str, row: int, column: int) -> None:
        self.__test_grid__.get_node(row, column).data = organism
