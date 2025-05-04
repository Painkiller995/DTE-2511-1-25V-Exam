class Node:
    def __init__(self, value, next=None, prev=None, parent=None):
        self._value = value
        self._next = next
        self._prev = prev
        self._parent = parent

    # Getter and setter for 'value'
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    # Getter and setter for 'next'
    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_node):
        self._next = next_node

    # Getter and setter for 'prev'
    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev_node):
        self._prev = prev_node

    # Getter and setter for 'parent'
    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent_node):
        self._parent = parent_node
