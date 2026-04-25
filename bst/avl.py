# 3rd party imports
from binarytree import Node

# User defined imports
from bst.logger import get_logger

log = get_logger()


class AvlTree:
    def __init__(self):
        self._root: Node | None = None  # Root node of the tree. Initially the tree root is null
        return

    def __str__(self):
        return self._root.__str__()  # Calling the __str__() function from binarytree package

    def search(self, value: int) -> None:
        """
        Searches for a value in the tree.
        :param value: The integer value to be searched for.
        """
        raise NotImplementedError  # TODO: Implementation

    def insert(self, value: int) -> None:
        """
        Inserts a new value into the bst. If the value already exists, it throws ValueError exception.
        :param value: The integer value to be inserted.
        :return: The height of the inserted new node.
        """
        # Note: It is possible to store additional fields on-the-fly into the binarytree.Node class. For example:
        #       self._root.rank = 0
        #       self._root.parent = parent_node

        raise NotImplementedError  # TODO: Implementation

    def delete(self, value: int) -> None:
        """
        Deletes a value from the tree.
        :param value: The integer value to be deleted.
        """
        raise NotImplementedError  # TODO: Implementation
