class TreeNode:
    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node

    def __str__(self):
        left_val = self._left._value if self._left else None
        right_val = self._right._value if self._right else None
        return f"TreeNode(value={self._value}, left={left_val}, right={right_val})"
