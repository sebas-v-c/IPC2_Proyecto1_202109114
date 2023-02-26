import os
from tkinter.filedialog import askopenfilename, asksaveasfile
from typing import Optional

from linkedList.linkedList import LinkedList
from samples.sample import Sample
import samples.sample_parser as smplp


sample_list = LinkedList()


# Main menu relataed operations down here


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


def main_menu(error: bool = False) -> None:
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
    execute_option(selected_option)


def execute_option(option: str) -> None:
    if option == "1":
        file_name: str = askopenfilename()
        if file_name:
            samples: LinkedList = smplp.parse_xml_sample_file(file_name)
            for sample_object in samples:
                sample_list.append(sample_object)
            print("Archivo cargado con exito!")
            pause()
        main_menu()

    elif option == "2":
        if len(sample_list) == 0:
            print("AUN NO SE HAN CARGADO MUESTRAS")
            pause()
            main_menu()
            return
        os.system("clear")
        sample_operations()
    elif option == "3":
        if len(sample_list) == 0:
            print("AUN NO SE HAN CARGADO MUESTRAS")
            pause()
            main_menu()
            return
        file = asksaveasfile(filetypes=[("XML File", "*.xml")], defaultextension=".xml")
        if file:
            smplp.save_samples_to_file(sample_list, file)
            print("ARCHIVO GUARDADO CON ÉXITO")
            pause()
        main_menu()

    elif option == "4":
        about()
        main_menu()
    elif option == "5":
        print("Hasta la proxima!")
    else:
        main_menu(error=True)


# Sample related operations down here

selected_sample: Optional[Sample] = None


def sample_operations(
    error: bool = False, selected_sample: Optional[Sample] = None
) -> None:
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

    if selected_sample is not None:
        print("Muestra seleccionada: ", f'"{selected_sample.sample_name}"')
    else:
        print("NO SE HA SELECCIONADO UNA MUESTRA")

    for i, option in enumerate(OPTIONS):
        print("\t", str(i + 1) + ". ", option)

    selected_option = input("\nIngresa una opción: ")
    execute_sample_options(selected_option)


def execute_sample_options(
    selected_option: str, selected_sample: Optional[Sample] = None
) -> None:
    if selected_option == "1":
        i = 0
        for sample in sample_list:
            i += 1
            print("\t", str(i) + ". ", sample.sample_name)
        option = int(input("Selecciona una muestra: ")) - 1
        try:
            selected_sample = sample_list[option].data
        except:
            print("OPCIÓN INVÁLIDA")
            pause()

        sample_operations(selected_sample=selected_sample)
        return

    if selected_option == "6":
        os.system("clear")
        main_menu()
        return

    if selected_sample is None:
        print("AÚN NO SE HA SELECCIONADO UNA MUESTRA")
        pause()
        sample_operations()
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
    sample_operations(error=True, selected_sample=selected_sample)


# Extra functions


def pause() -> None:
    input("Presione una tecla para continuar...")
    os.system("clear")
