class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.val = val


class Tree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.val:
            if node.l:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if self.root:
            return self._find(val, self.root)

    def _find(self, val, node):
        if val == node.val:
            return node
        elif val < node.val and node.l:
            return self._find(val, node.l)
        elif val > node.val and node.r:
            return self._find(val, node.r)

    def delete_tree(self):
        if self.root:
            self.root = None

    def view_tree(self):
        if self.root:
            self._view_tree(self.root)

    def _view_tree(self, node):
        if node:
            self._view_tree(node.l)
            print(node.val, end="\n")
            self._view_tree(node.r)


tree = Tree()
tree.add(10)
tree.add(1)
tree.add(8)
tree.add(7)
tree.add(1)
print(tree.find(10))
print(tree.find(6))
tree.view_tree()
tree.delete_tree()
print(tree.view_tree())
