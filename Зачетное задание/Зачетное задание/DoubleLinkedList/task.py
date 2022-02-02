from typing import Any, Iterable, Optional

from collections.abc import MutableSequence

from node import Node


class LinkedList(MutableSequence):
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0
        self._head: Optional[Node] = None
        self.tail = self._head

        if data is not None:
            for value in data:
                self.append(value)

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    @staticmethod
    def _linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"

    def insert (self, index: int, value: Any) -> None:
        insert_node = Node(value)
        if index == 0:
            insert_node.next = self._head
            self.head = insert_node
            self._linked_nodes(self._head, insert_node.next)
            self._len += 1
        elif index >= self._len:
            self.append(value)
        else:
            prev_node = self._step_by_step_on_nodes(index - 1)
            next_node = prev_node.next
            self._linked_nodes(prev_node, insert_node)
            self._linked_nodes(insert_node, next_node)
            self._len += 1

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1

    def index (self, value: Any) -> int:
        """Метод возвращает индекс узла по указанному значению"""
        i = 0
        while i <self._len:
            node = self._step_by_step_on_nodes(i)
            if node.value == value:
                break
            else:
                i += 1
        if i == self._len:
            raise ValueError
        return i

    def count(self, sub: Any) -> int:
        """Метод возвращает колическтво вхождений указанного значения в список"""
        i = 0
        sum_ = 0
        while i < self._len:
            node = self._step_by_step_on_nodes(i)
        else:
            i += 1
        return sum_

    def extend(self, value: list) -> None:
        """ Добавление всех элементов в конец связанного списка"""
        for i in range(len(value)):
            self.append(value[i])

    def pop(self, index: int) -> Node:
        """Удаляет элемент из списка и возвращает элемент"""
        node = self._step_by_step_on_nodes(index)
        self.__delitem__(index)
        return node.value


#class DoubleLinkedNode(Node):
#    def __init__(self, value: Any, prev: Optional["Node"] = None, next_: Optional["Node"] = None):
#        super().__init__(value, next_)
#        self.prev = prev

#    @property
#    def prev(self):
#        return self._prev

#    @prev.setter
#    def prev(self, prev: Optional["Node"]):
#        self.is_valid(prev)
#        self._prev = prev

#    def __repr__(self) -> str:
#        next_prev = None if self.prev is None else f"DoubleLinkedNode({self.prev})"
#        next_repr = None if self.next is None else f"DoubleLinkedNode({self.next})"  # make all

#        return f"DoubleLinkedNode({self.value}, {next_prev}, {next_repr})"



class DoubleLinkedList(LinkedList):
    node_class = DoubleLinkedNode

    #super().__init__()

    @staticmethod
    def linked_nodes(left_node: DoubleLinkedNode, right_node: Optional[DoubleLinkedNode] = None) -> None:
        left_node.next = right_node
        right_node.prev = left_node

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = DoubleLinkedNode(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1


if __name__ == "__main__":
    list_ = ['a', 'b', 'c']
    ll = LinkedList(list_)
    print(ll.__getitem__(1))
    print(ll.__setitem__(1, 'v'))
    print(ll)
    ll.__delitem__(1)
    print(ll)
    ll.insert(3, 'b')
    print(ll)
    print(len(ll))
    ll.append('d')
    print(ll)
    print.index('b')
    print(ll.count('b'))
    ll.extend(['df', 'as'])
    print(ll)
    print(ll.pop(4))
    print(ll)