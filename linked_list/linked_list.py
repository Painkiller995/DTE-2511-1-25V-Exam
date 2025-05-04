from node import Node


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    def add_first(self, value):
        new_node = Node(value)
        if self.is_empty():
            self._head = self._tail = new_node
            return
        new_node.next = self._head
        self._head.prev = new_node
        self._head = new_node

    def add_last(self, value):
        new_node = Node(value)
        if self.is_empty():
            self._head = self._tail = new_node
            return
        self._tail.next = new_node
        self._tail = new_node

    def get_first(self):
        return self._head

    def get_last(self):
        return self._tail

    def is_empty(self):
        return not self.get_first()

    def clear(self):
        self._head = self._tail = None

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

    linked_list.get_first()


if __name__ == "__main__":
    main()
