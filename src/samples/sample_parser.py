from linkedList.linkedList import LinkedList
import xml.etree.ElementTree as ET
import xml.dom.minidom
from linkedList.node import MatrixNode

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
            organism_code = str(living_cell[2].text)
            new_sample.place_living_cell(organism_code, row - 1, column - 1)

        new_sample.organisms = organisms_list
        sample_list.append(new_sample)

    return sample_list


def generate_xml_string(sample_list: LinkedList) -> str:
    root = ET.Element("datosMarte")
    organisms_list_element = ET.Element("listaOrganismos")
    samples_list_element = ET.Element("listadoMuestras")
    root.append(organisms_list_element)
    root.append(samples_list_element)

    organisms_list = LinkedList()

    for sample in sample_list:
        for organism in sample.organisms:
            exist = False
            for local_organism in organisms_list:
                if local_organism.code == organism.code:
                    exist = True
                    break
            if not exist:
                organisms_list.append(organism)

    for organism in organisms_list:
        organism_element = ET.Element("organismo")
        ET.SubElement(organism_element, "codigo").text = organism.code
        ET.SubElement(organism_element, "nombre").text = organism.name
        organisms_list_element.append(organism_element)

    for sample in sample_list:
        sample_element = ET.Element("muestra")
        ET.SubElement(sample_element, "codigo").text = sample.sample_code
        ET.SubElement(sample_element, "descripcion").text = sample.sample_description
        rows, columns = sample.get_grid_dimentions()
        ET.SubElement(sample_element, "filas").text = str(rows)
        ET.SubElement(sample_element, "columnas").text = str(columns)

        living_cells_list = ET.SubElement(sample_element, "listadoCeldasVivas")
        for row in range(rows):
            for column in range(columns):
                current_node: MatrixNode = sample.get_cell(row, column)
                if current_node.data is not None:
                    for organism in organisms_list:
                        if organism.code == current_node.data:
                            living_cell = ET.SubElement(living_cells_list, "celdaViva")
                            ET.SubElement(living_cell, "fila").text = str(row + 1)
                            ET.SubElement(living_cell, "columna").text = str(column + 1)
                            ET.SubElement(
                                living_cell, "codigoOrganismo"
                            ).text = current_node.data
        samples_list_element.append(sample_element)

    return xml.dom.minidom.parseString(ET.tostring(root)).toprettyxml()
