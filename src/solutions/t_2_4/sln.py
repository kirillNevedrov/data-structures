from src.linked_list import LinkedList


def partition(list: LinkedList[int], value: int) -> None:
    first_left_part_node = None
    last_left_part_node = None
    first_right_part_node = None
    last_right_part_node = None

    node = list.root

    while node:
        if node.value < value:
            if not first_left_part_node:
                first_left_part_node = node

            if last_left_part_node:
                last_left_part_node.next = node

            last_left_part_node = node
        else:
            if not first_right_part_node:
                first_right_part_node = node

            if last_right_part_node:
                last_right_part_node.next = node

            last_right_part_node = node

        node = node.next

    if first_left_part_node:
        list.root = first_left_part_node
    elif first_right_part_node:
        list.root = first_right_part_node

    if last_left_part_node and first_right_part_node:
        last_left_part_node.next = first_right_part_node
