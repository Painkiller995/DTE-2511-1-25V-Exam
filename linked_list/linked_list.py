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
        new_node.prev = self._tail
        self._tail = new_node

    def remove_first(self):
        if self.is_empty():
            return None
        current_head_value = self._head.value
        self._head: Node = self._head.next
        self._head.prev = None
        return current_head_value

    def remove_last(self):
        if self.is_empty():
            return None
        current_tail_value = self._tail.value
        self._tail: Node = self._tail.prev
        self._tail.next = None
        return current_tail_value

    def get_first(self):
        return self._head.value if self._head else None

    def get_last(self):
        return self._tail.value if self._tail else None

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
    linked_list.remove_first()
    linked_list.remove_last()
    for node in linked_list:
        print(node.value)


if __name__ == "__main__":
    main()
