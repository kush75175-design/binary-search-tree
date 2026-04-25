# 3rd party imports
from binarytree import Node

# User defined imports
from bst.logger import get_logger

log = get_logger()


class BinarySearchTree:
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
        node: Node | None = self._root  # Initialize to the root of the tree

        # Loop from tree root to a leaf node searching for the target value
        while node is not None:
            if node.value == value:
                log.success(f'Search found value: {value}')
                return  # Found the value, return now
            elif value < node.value:
                node = node.left  # Search in the left subtree
            else:
                node = node.right  # Search in the right subtree

        log.warning(f"Search returned without finding value: {value} within tree")
        return  # Value is not present in the tree

    def insert(self, value: int) -> None:
        """
        Inserts a new value into the bst. If the value already exists, it throws ValueError exception.
        :param value: The integer value to be inserted.
        """
        # Special case: tree is empty
        if self._root is None:
            self._root = Node(value)
            return

        node: Node | None = self._root  # Initialize "node" to the root of the tree

        # Loop from tree root to a leaf node searching for the target value
        while node is not None:
            if node.value == value:
                log.warning(f"Not inserting value: {value} as it already exists within tree")
                break
            elif value < node.value:
                if node.left is None:  # Left subtree is empty
                    node.left = Node(value)  # Insert the value as the left child of this node
                    break  # Done inserting the node, break out of the loop
                else:
                    node = node.left  # Search in the left subtree
            else:
                if node.right is None:  # Right subtree is empty
                    node.right = Node(value)  # Insert the value as the right child of this node
                    break  # Done inserting the node, break out of the loop
                else:
                    node = node.right  # Search in the right subtree

        log.success(f'Inserted value: {value} into the tree')
        return

    def _get_replacement_node(self, node: Node) -> Node:
        """
        The replacement node is the node that is biggest (i.e. value) within this node's left subtree.
        Biggest node is same as the rightmost node in the subtree.
        :param node: Root of this subtree. Never None.
        :return: The replacement node within the subtree. Never None.
        """
        assert node is not None  # Sanity check. This function is called for valid nodes only.
        while node.right is not None:  # Find the biggest in this subtree (follow the right edges)
            node = node.right

        return node

    def _delete_in_subtree(self, node: Node, value: int) -> Node | None:
        """
        :param node: Root of this subtree. Could be None.
        :param value: The integer value to be deleted from this subtree. Value may or may not exist in subtree.
        :return: The new (if need be) root of this subtree. Could be None.
        """
        if node is None:  # Special case. Early exit
            return node

        if value < node.value:
            if node.left is None:
                log.warning(f"Skip deletion as value {value} is not found within the tree")
                return None
            else:
                node.left = self._delete_in_subtree(node.left, value)  # Search in the left subtree
        elif value > node.value:
            if node.right is None:
                log.warning(f"Skip deletion as value {value} is not found within the tree")
                return None
            else:
                node.right = self._delete_in_subtree(node.right, value)  # Search in the right subtree
        else:
            # Current node is the target node that needs to be deleted
            if node.left is None:  # If no left child, then simply use the right child to replace current node
                log.success(f'Deleted value: {value} from the tree')
                return node.right
            elif node.right is None:  # If no right child, then simply use the left child to replace current node
                log.success(f'Deleted value: {value} from the tree')
                return node.left
            else:  # Both children available. Will need to swap values and recurse further
                replacement: Node = self._get_replacement_node(node.left)
                node.value, replacement.value = replacement.value, node.value  # Swap values
                node.left = self._delete_in_subtree(node.left, value)  # Recurse further

        return node

    def delete(self, value: int) -> None:
        """
        Deletes a value from the tree.
        :param value: The integer value to be deleted.
        """
        self._root = self._delete_in_subtree(self._root, value)  # Call this recursive function for deletion
        return
