from node import Node


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    def add_first(self, value):
        new_node = Node(value)

        if not self._head:
            self._head = self._tail = new_node
            return
        # Set current head to the new node
        new_node.next = self._head
        # Set the prev to the new node
        self._head.prev = new_node
        # Update the head to the new node
        self._head = new_node

    def __iter__(self):
        current_node = self._head
        while current_node:
            yield current_node
            current_node = current_node.next


def main():
    linked_list = LinkedList()
    linked_list.add_first(2)
    linked_list.add_first(1)
    linked_list.add_first(3)
    for node in linked_list:
        print(node.value)


if __name__ == "__main__":
    main()
