from linkedList.linkedList import LinkedList, LinkedMatrix
import random
from samples.sample import Sample
import subprocess


DEFAULT_CONF = "\n".join(
    [
        "digraph {",
        '\tgraph [pad="0.1", nodesep="0.5", ranksep="2"];',
        "\tnode [shape=plain]",
        "\trankdir=LR;",
    ]
)

FULL_FORMAT_STR = lambda x: f"{DEFAULT_CONF}\n{x}\n" + "}"


def create_graphviz_table(sample: Sample, tables_name="Sample") -> str:
    # A list with a organism name and color
    organisms_color: LinkedList = LinkedList()
    for organism in sample.organisms:
        # a tupple with an organism code and a random color
        echo_color = subprocess.Popen(
            ["echo", "-n", f"{organism.code}"], stdout=subprocess.PIPE
        )
        get_hash = subprocess.Popen(
            ["md5sum"], stdin=echo_color.stdout, stdout=subprocess.PIPE
        )
        cuted_color = subprocess.Popen(
            ["cut", "-c1-6"], stdin=get_hash.stdout, stdout=subprocess.PIPE
        )

        color, err = cuted_color.communicate()
        color = color.decode("utf-8")

        hex_color = f"#{color}"
        organisms_color.append((organism.code, hex_color))

    html_sample_table = "\n".join(
        [
            f"{tables_name}Table [label=<",
            '<table border="0" cellborder="1" cellspacing="0" cellpadding="25">\n',
        ]
    )

    rows, columns = sample.get_grid_dimentions()
    for row in range(rows):
        html_sample_table += "\t<tr>\n"
        for column in range(columns):
            organism_name = sample.get_cell(row, column).data
            if organism_name is None:
                html_sample_table += "\t\t<td></td>\n"
                continue

            for organism in organisms_color:
                if organism[0] == organism_name:
                    html_sample_table += f'\t\t<td bgcolor="{organism[1]}"></td>\n'
                    break

        html_sample_table += "\t</tr>\n"

    html_sample_table += "</table>\n>];"

    html_organism_table = "\n".join(
        [
            f"{tables_name}Organism [label=<",
            '<table border="0" cellborder="1" cellspacing="0" cellpadding="5">\n',
        ]
    )
    for organism in organisms_color:
        html_organism_table += (
            f'<tr><td bgcolor="{organism[1]}">{organism[0]}</td></tr>'
        )

    html_organism_table += "</table>\n>];"

    last_line = f"{tables_name}Table -> {tables_name}Organism [style=invis];"

    return "\n".join([html_sample_table, html_organism_table, last_line])


def create_marked_graphviz_table(
    sample: Sample, marks: LinkedList, tables_name="Organism"
) -> str:
    # A list with a organism name and color
    organisms_color: LinkedList = LinkedList()
    for organism in sample.organisms:
        # a tupple with an organism code and a random color
        echo_color = subprocess.Popen(
            ["echo", "-n", f"{organism.code}"], stdout=subprocess.PIPE
        )
        get_hash = subprocess.Popen(
            ["md5sum"], stdin=echo_color.stdout, stdout=subprocess.PIPE
        )
        cuted_color = subprocess.Popen(
            ["cut", "-c1-6"], stdin=get_hash.stdout, stdout=subprocess.PIPE
        )

        color, err = cuted_color.communicate()
        color = color.decode("utf-8")

        hex_color = f"#{color}"
        organisms_color.append((organism.code, hex_color))

    html_sample_table = "\n".join(
        [
            f"{tables_name}Table [label=<",
            '<table border="0" cellborder="1" cellspacing="0" cellpadding="25">\n',
        ]
    )

    rows, columns = sample.get_grid_dimentions()
    for row in range(rows):
        html_sample_table += "\t<tr>\n"
        for column in range(columns):
            organism_name = sample.get_cell(row, column).data
            marked = False
            for mark in marks:
                if mark[0] == row and mark[1] == column:
                    html_sample_table += '\t\t<td bgcolor="#00000"></td>\n'
                    marked = True
                    break

            if marked:
                continue
            if organism_name is None:
                html_sample_table += "\t\t<td></td>\n"
                continue
            for organism in organisms_color:
                if organism[0] == organism_name:
                    html_sample_table += f'\t\t<td bgcolor="{organism[1]}"></td>\n'
                    break

        html_sample_table += "\t</tr>\n"

    html_sample_table += "</table>\n>];"

    html_organism_table = "\n".join(
        [
            f"{tables_name}Organism [label=<",
            '<table border="0" cellborder="1" cellspacing="0" cellpadding="5">\n',
        ]
    )
    for organism in organisms_color:
        html_organism_table += (
            f'<tr><td bgcolor="{organism[1]}">{organism[0]}</td></tr>'
        )

    html_organism_table += "</table>\n>];"

    last_line = f"{tables_name}Table -> {tables_name}Organism [style=invis];"

    return "\n".join(
        [
            html_sample_table,
            html_organism_table,
            last_line,
            'Title [label=<<table bordet="0" cellborder="1" cellspacing="0" cellpadding="10">\n',
            "<tr><td>Los cuadros en negro son los lugares donde pueden prosperar los organismos;</td></tr>\n",
            "</table>>];",
            "Title;",
        ]
    )
