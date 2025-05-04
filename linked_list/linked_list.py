from node import Node


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0

    def add_first(self, value):
        new_node = Node(value)
        if self.is_empty():
            self._head = self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        self._count += 1

    def add_last(self, value):
        new_node = Node(value)
        if self.is_empty():
            self._head = self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
        self._count += 1

    def add(self, value):
        return self.add_last(value)

    def remove_first(self):
        if self.is_empty():
            return None
        current_head_value = self._head.value
        self._head = self._head.next
        if self._head:
            self._head.prev = None
        else:
            self._tail = None
        self._count -= 1
        return current_head_value

    def remove_last(self):
        if self.is_empty():
            return None
        current_tail_value = self._tail.value
        self._tail = self._tail.prev
        if self._tail:
            self._tail.next = None
        else:
            self._head = None
        self._count -= 1
        return current_tail_value

    def get_first(self):
        return self._head.value if self._head else None

    def get_last(self):
        return self._tail.value if self._tail else None

    def size(self):
        return self._count

    def is_empty(self):
        return self._count == 0

    def clear(self):
        self._head = self._tail = None
        self._count = 0

    def __iter__(self):
        current_node = self._head
        while current_node:
            yield current_node.value
            current_node = current_node.next

    def __eq__(self, other):
        if not isinstance(other, LinkedList):
            return False
        if self.size() != other.size():
            return False
        return all(a == b for a, b in zip(self, other))

    def __len__(self):
        return self._count

    def __str__(self):
        return "[" + ", ".join(str(v) for v in self) + "]"

    def __repr__(self):
        return f"LinkedList({list(self)})"


def main():
    linked_list = LinkedList()
    linked_list.add_last(8)
    linked_list.add_last(9)
    linked_list.add_first(7)

    for value in linked_list:
        print(value)

    print("-" * 50)
    print("Size:", linked_list.size())
    print("First:", linked_list.get_first())
    print("Last:", linked_list.get_last())
    print("As list:", list(linked_list))
    print("String repr:", str(linked_list))
    print("Min:", min(linked_list))
    print("Max:", max(linked_list))


if __name__ == "__main__":
    main()
