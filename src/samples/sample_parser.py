from linkedList.linkedList import LinkedList
import xml.etree.ElementTree as ET

from samples.organism import Organism
from samples.sample import Sample


def parse_xml_sample_file(file_name: str) -> LinkedList:
    xml_tree = ET.parse(file_name)
    root = xml_tree.getroot()
    sample_list: LinkedList = LinkedList()
    organisms_list: LinkedList = LinkedList()

    for organism in root[0]:
        organisms_list.append(Organism(str(organism[0].text), str(organism[1].text)))

    for sample in root[1]:
        new_sample = Sample(
            str(sample[0].text),
            str(sample[1].text),
            int(str(sample[2].text)),
            int(str(sample[3].text)),
        )
        for living_cell in sample[4]:
            row = int(str(living_cell[0].text))
            column = int(str(living_cell[1].text))
            organism_code = str(living_cell[1].text)
            new_sample.place_living_cell(organism_code, row, column)

        new_sample.organisms = organisms_list
        sample_list.append(new_sample)

    return sample_list


def save_samples_to_file(sample_list: LinkedList, file_name: str) -> None:
    pass
