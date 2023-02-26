import os
from tkinter.filedialog import askopenfilename, asksaveasfile
from typing import Optional

from linkedList.linkedList import LinkedList
from samples.sample import Sample
import samples.sample_parser as smplp


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
            "Guardar muestras actuales como nuevo archivo",
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
                filetypes=[("XML File", "*.xml")], defaultextension=".xml"
            )
            print(type(file))
            if file:
                smplp.save_samples_to_file(self.sample_list, file.name)
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

    def sample_operations(self, error: bool = False) -> None:
        if error:
            print("\n\n\t\tOPCION INCORRECTA\n")
            pause()

        OPTIONS = [
            "Seleccionar una muestra",  # Select a sample from the sample linked list
            "Identificar celdas para vida prosperable",  # Identify the cells where an organism could survive
            "Colocar organismo en una celda",  # put an organism in a cell
            "Actualizar información de la muestra",  # Update this specific sample
            "Crear nueva muestra con la muestra actual",  # create a new sample in base of the changes made to this sample
            "Regresar",
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
        if selected_option == "1":
            i = 0
            for sample in self.sample_list:
                i += 1
                print("\t", str(i) + ". ", sample.sample_code)
            option = int(input("Selecciona una muestra: ")) - 1
            try:
                self.selected_sample = self.sample_list[option].data
            except:
                print("OPCIÓN INVÁLIDA")
                pause()

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
            # TODO
            return
        elif selected_option == "3":
            # TODO
            return
        elif selected_option == "4":
            # TODO
            return
        elif selected_option == "5":
            # TODO
            return

        # if everything of the above fails
        self.sample_operations(error=True)
