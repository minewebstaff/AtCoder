n, q = (int(x) for x in input().split())

class Node:
    def __init__(self, label):
        self.label = label
        self.small: Node
        self.big: Node

    def add_pre(self, anode):
        q = f"? {self.label} {anode.label}"
        return q

    def add(self, anode, comparator):
        if comparator == "<":
            if self.small is None:
                self.small = anode
            else:
                



