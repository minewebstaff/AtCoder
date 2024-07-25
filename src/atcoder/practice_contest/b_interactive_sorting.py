n, q = (int(x) for x in input().split())

class Node:
    def __init__(self, label):
        self.label = label
        self.small: Node = None
        self.big: Node = None

    def add(self, new_node:Node, hikaku: str) -> str:
        if hikaku == "<":
            if self.small is None:
                self.small = new_node
