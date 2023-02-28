import os
from tkinter.filedialog import askopenfilename, asksaveasfile
from typing import Optional

from linkedList.linkedList import LinkedList
from samples.organism import Organism
from samples.sample import Sample
import samples.sample_parser as smplp
import copy


def pause() -> None:
    input("Presione una tecla para continuar...")
    os.system("clear")


def about() -> None:
    os.system("clear")
    print("------------------------------------------------")
    print("|Introducción a la Programación y Computación 2|")
    print("|                  Seccion: D                  |")
    print("|               Carnet: 202109114              |")
    print("|Nombre: Sebastian Alejandro  Vásquez Cartagena|")
    print("|                                              |")
    print("|                  Proyecto 1                  |")
    print("------------------------------------------------")
    pause()


# Main menu relataed operations down here


class MainMenu:
    def __init__(self, sample_list: LinkedList = LinkedList()) -> None:
        self.sample_list = sample_list

    def main_menu(self, error: bool = False) -> None:
        if error:
            print("\n\n\t\tOPCION INCORRECTA\n")
            pause()

        OPTIONS = [
            "Cargar un archivo de muestra",
            "Simulador de muestras",
            "Exportar muestras a un xml",
            "Acerca de",
            "Salir",
        ]
        # os.system("clear")
        print(
            r"""
 ___       ________   ________
|\  \     |\   ___  \|\   ____\
\ \  \    \ \  \\ \  \ \  \___|
 \ \  \    \ \  \\ \  \ \  \  ___
  \ \  \____\ \  \\ \  \ \  \|\  \
   \ \_______\ \__\\ \__\ \_______\
    \|_______|\|__| \|__|\|_______|
        """
        )

        for i, option in enumerate(OPTIONS):
            print("\t", str(i + 1) + ". ", option)

        selected_option = input("\nIngresa una opción: ")
        self.execute_option(selected_option)

    def execute_option(self, option: str) -> None:
        if option == "1":
            file_name: str = askopenfilename()
            if file_name:
                samples: LinkedList = smplp.parse_xml_sample_file(file_name)
                for sample_object in samples:
                    self.sample_list.append(sample_object)
                print("Archivo cargado con exito!")
                pause()
            self.main_menu()

        elif option == "2":
            if len(self.sample_list) == 0:
                print("AUN NO SE HAN CARGADO MUESTRAS")
                pause()
                self.main_menu()
                return
            os.system("clear")
            sample_menu = SampleMenu(self.sample_list)
            sample_menu.sample_operations()
            self.sample_list = sample_menu.sample_list
            self.main_menu()
            return
        elif option == "3":
            if len(self.sample_list) == 0:
                print("AUN NO SE HAN CARGADO MUESTRAS")
                pause()
                self.main_menu()
                return
            file = asksaveasfile(
                mode="w", filetypes=[("XML File", "*.xml")], defaultextension=".xml"
            )
            if file:
                xml_string = smplp.generate_xml_string(self.sample_list)
                file.write(xml_string)
                file.close()
                print("ARCHIVO GUARDADO CON ÉXITO")
                pause()
            self.main_menu()
        elif option == "4":
            about()
            self.main_menu()
        elif option == "5":
            print("Hasta la proxima!")
        else:
            self.main_menu(error=True)


# Sample related operations down here


class SampleMenu:
    def __init__(self, sample_list: LinkedList) -> None:
        self.sample_list = sample_list
        self.selected_sample: Optional[Sample] = None
        self.sample_can_survive = False
        self.selected_organisms = LinkedList()
        self.modified_sample: Optional[Sample] = None
        self.cell_to_live_for: LinkedList = LinkedList()

    def sample_operations(self, error: bool = False) -> None:
        if error:
            print("\n\n\t\tOPCION INCORRECTA\n")
            pause()

        OPTIONS = [
            "Seleccionar una muestra",  # 1
            "Identificar celdas para vida prosperable",  # 2
            "Colocar organismo en una celda",  # 3
            "Actualizar información de la muestra",  # 4
            "Crear nueva muestra con la muestra actual",  # 5
            "Regresar",  # 6
        ]
        # use "deepcopy" to create a complete diferent object from the one selected
        print(
            r"""
 _____ _____ _____ _____ __    _____ ____  _____ _____
|   __|     |     |  |  |  |  |  _  |    \|     | __  |
|__   |-   -| | | |  |  |  |__|     |  |  |  |  |    -|
|_____|_____|_|_|_|_____|_____|__|__|____/|_____|__|__|
 ____  _____
|    \|   __|
|  |  |   __|
|____/|_____|
 _____ _____ _____ _____ _____ _____ _____ _____
|     |  |  |   __|   __|_   _| __  |  _  |   __|
| | | |  |  |   __|__   | | | |    -|     |__   |
|_|_|_|_____|_____|_____| |_| |__|__|__|__|_____|

            """
        )

        selected_option: str = "0"

        if self.selected_sample is not None:
            print("Muestra seleccionada: ", f'"{self.selected_sample.sample_code}"')
        else:
            print("NO SE HA SELECCIONADO UNA MUESTRA")

        for i, option in enumerate(OPTIONS):
            print("\t", str(i + 1) + ". ", option)

        selected_option = input("\nIngresa una opción: ")
        self.execute_sample_options(selected_option)

    def execute_sample_options(self, selected_option: str) -> None:
        """Given an option execute the corresponend code"""
        if selected_option == "1":
            i = 0
            for sample in self.sample_list:
                i += 1
                print("\t", str(i) + ". ", sample.sample_code)
            try:
                option = int(input("Selecciona una muestra: ")) - 1
                temp_sample = self.sample_list[option].data
                rows, columns = temp_sample.get_grid_dimentions()
                self.selected_sample = Sample(
                    temp_sample.sample_code,
                    temp_sample.sample_description,
                    rows,
                    columns,
                )
                self.selected_sample.organisms = temp_sample.organisms
                self.selected_sample.test_grid = temp_sample.copy_test_grid()
                self.selected_organisms = self.selected_sample.organisms
            except:
                print("OPCIÓN INVÁLIDA")
                pause()

            # print(len(self.selected_organisms))
            self.cell_to_live_for = self._verify_valid_sample()
            self.sample_operations()
            return

        if selected_option == "6":
            os.system("clear")
            return

        if self.selected_sample is None:
            print("AÚN NO SE HA SELECCIONADO UNA MUESTRA")
            pause()
            self.sample_operations()
            return
        elif selected_option == "2":
            if len(self.cell_to_live_for) == 0:
                print("No existe un lugar donde puedan prosperar las muestras")
                pause()
                self.sample_operations()
                return

            # TODO call graphviz code idk
            for cell in self.cell_to_live_for:
                pass

            self.sample_operations()
            return
        elif selected_option == "3":
            os.system("clear")
            # if not self.sample_can_survive:
            #     print("NINGUNA CELULA SOBREVIRA CON MUESTRA ACTUAL")
            #     pause()
            #     self.sample_operations()
            #     return

            selected_organism: Optional[Organism] = None
            i = 0
            for organism in self.selected_organisms:
                i += 1
                print("\t", str(i) + ". ", organism.code)

            try:
                option = int(input("Selecciona un organismo: ")) - 1
                selected_organism = self.selected_organisms[option].data
            except:
                print("OPCION INVALIDA")
                pause()
                self.sample_operations()
                return

            rows, columns = self.selected_sample.get_grid_dimentions()
            print(f"Las dimensiones de la lista son ({rows}, {columns})")
            print("Ingrese donde desea insertar la celda")
            row = 0
            column = 0
            try:
                row = int(input("Ingrese fila: ")) - 1
                column = int(input("Ingrese columna: ")) - 1
                if row >= rows or column >= columns:
                    raise Exception
            except:
                print("Valores Equivocados!")
                pause()
                self.sample_operations()
                return

            rows, columns = self.selected_sample.get_grid_dimentions()
            sample_copy = Sample(
                self.selected_sample.sample_code,
                self.selected_sample.sample_description,
                rows,
                columns,
            )
            sample_copy.test_grid = self.selected_sample.copy_test_grid()

            can_live = sample_copy.simulate_sample_at_cell(
                row, column, selected_organism.code
            )
            if can_live:
                sample_copy.get_cell(row, column).data = selected_organism.code
            # TODO
            # generated_sample = graphviz
            self.selected_sample.test_grid.display_matrix(size=4)
            print("")
            sample_copy.test_grid.display_matrix(size=4)

            self.selected_sample.test_grid = sample_copy.copy_test_grid()
            self.sample_operations()
            return

        elif selected_option == "4":
            i = 0
            for sample in self.sample_list:
                if sample.sample_code == self.selected_sample.sample_code:
                    self.sample_list[i].data.test_grid = self.selected_sample.test_grid

            print("Cambios guardados con exito")
            pause()
            self.sample_operations()
            return
        elif selected_option == "5":
            os.system("clear")

            new_code = input("Ingresa el codigo de la nueva muestra: ")
            for sample in self.sample_list:
                if sample.sample_code == new_code:
                    print("ESTE CODIGO YA EXISTE")
                    pause()
                    self.sample_operations()
                    return
            new_description = input("Ingresa unaa descripcion para la nueva muestra: ")
            rows, columns = self.selected_sample.get_grid_dimentions()
            new_sample = Sample(new_code, new_description, rows, columns)
            new_sample.test_grid = self.selected_sample.copy_test_grid()
            self.sample_list.append(new_sample)
            self.sample_operations()
            return

        # if everything of the above fails
        self.sample_operations(error=True)

    def _verify_valid_sample(self) -> LinkedList:
        surviving_samples = LinkedList()
        rows, columns = self.selected_sample.get_grid_dimentions()
        for organism in self.selected_organisms:
            for row in range(rows):
                for column in range(columns):
                    can_live = self.selected_sample.simulate_sample_at_cell(
                        row, column, organism.code
                    )
                    if can_live:
                        surviving_samples.append((row, column, organism.code))
                        self.sample_can_survive = True

                    # new_sample = self.selected_sample.simulate_sample_at(
                    #     rows, columns, organism.code
                    # )
                    # if new_sample:
                    #     surviving_samples.append(new_sample)
                    #     self.sample_can_survive = True

        return surviving_samples
