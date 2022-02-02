from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next_

    def __str__(self) -> str:
        return f"{self.value}"

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next_ is None else f"Node({self.value})"

    @classmethod
    def is_valid(cls, node: Any) -> None:
        if not isinstance(node, (type(None), cls)):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_


class DoubleLinkedNode(Node):
    def __init__ (self, value, next_=None, prev=None):
        super().__init__(value, next_)
        self.prev = prev

    def __repr__(self) -> str:
        name = self.__class__.__name__
        return f"{name}({self.value}, {None})" if self.next is None else f"{name}({self.value}, DoubleLinkedNode({self.next}))"

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev: Optional["DoubleLinkedNode"]):
        self.is_valid(prev)
        self._prev = prev


if __name__ == "__main__":
    node = Node(5)
    print(str(node))
    print(repr(node))
