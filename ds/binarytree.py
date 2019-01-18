class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def pre_order_depth_first_traversal(self) -> list:
        return self._pre_order_depth_first_traversal_recursive_helper_function(self.root, [])

    def _pre_order_depth_first_traversal_recursive_helper_function(self, node: Node, values: list) -> list:
        if node is None:
            return values
        values.append(node.value)
        self._pre_order_depth_first_traversal_recursive_helper_function(node.left, values)
        self._pre_order_depth_first_traversal_recursive_helper_function(node.right, values)
        return values

    def in_order_depth_first_traversal(self) -> list:
        return self._in_order_depth_first_traversal_recursive_helper_function(self.root, [])

    def _in_order_depth_first_traversal_recursive_helper_function(self, node: Node, values: list) -> list:
        if node is None:
            return values
        self._in_order_depth_first_traversal_recursive_helper_function(node.left, values)
        values.append(node.value)
        self._in_order_depth_first_traversal_recursive_helper_function(node.right, values)
        return values

    def out_order_depth_first_traversal(self):
        return self._out_order_depth_first_traversal_recursive_helper_function(self.root, [])

    def _out_order_depth_first_traversal_recursive_helper_function(self, node: Node, values: list):
        if node is None:
            return values
        self._out_order_depth_first_traversal_recursive_helper_function(node.left, values)
        self._out_order_depth_first_traversal_recursive_helper_function(node.right, values)
        values.append(node.value)
        return values

    def test(self, node: Node):
        yield node.value
        self.test(node.left)
        self.test(node.right)

    def breadth_first_traversal(self):
        pass
