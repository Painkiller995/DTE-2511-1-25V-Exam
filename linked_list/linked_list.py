from node import Node


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    def is_empty(self):
        return not self._head

    def add_first(self, value):
        new_node = Node(value)

        if self.is_empty():
            self._head = self._tail = new_node
            return
        # Set current head to the new node
        new_node.next = self._head
        # Set the prev to the new node
        self._head.prev = new_node
        # Update the head to the new node
        self._head = new_node

    def add_last(self, value):
        new_node = Node(value)
        if self.is_empty():
            self._head = self._tail = new_node
            return

        self._tail.next = new_node
        self._tail = new_node

    def __iter__(self):
        current_node = self._head
        while current_node:
            yield current_node
            current_node = current_node.next


def main():
    linked_list = LinkedList()
    linked_list.add_last(8)
    linked_list.add_last(9)
    linked_list.add_first(7)
    for node in linked_list:
        print(node.value)


if __name__ == "__main__":
    main()
