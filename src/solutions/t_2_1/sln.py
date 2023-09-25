from src.linked_list import LinkedList


def remove_duplicates(list: LinkedList) -> None:
    p1 = list.root
    while p1:
        p2 = p1.next
        prev = p1
        while p2:
            if p2.value == p1.value:
                prev.next = p2.next
            else:
                prev = p2

            p2 = p2.next
        
        p1 = p1.next

