class Node:
    def __init__(self, value, next=None, prev=None):
        self._value = value
        self._next = next
        self._prev = prev

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

    def __str__(self):
        return self.value
