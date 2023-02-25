#!/usr/bin/env python3

from linkedList.linkedList import LinkedList, LinkedMatrix


def main():
    # matrix = LinkedMatrix(5, 10)
    # matrix.display_matrix()
    list = LinkedList()
    list.preppend(123)
    list.preppend(456)
    list.append(789)

    for node in reversed(list):
        print(node.data)


if __name__ == "__main__":
    main()
