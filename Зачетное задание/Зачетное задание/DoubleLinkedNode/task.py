class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: float, next_=None):
        self.value = value
        self.next_ = next_

    def __str__(self) -> str:
        return f"{self.value}"

    def __repr__(self) -> str:
        return f"Node({self.value}, {self.next_})"


class DoubleLinkedNode(Node):
    ...


if __name__ == "__main__":
    node = Node(5)
    print(str(node))
    print(repr(node))
