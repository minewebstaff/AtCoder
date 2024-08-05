class Node:
    def __init__(self, label):
        self.label = label
        # self.root: Node = self if is_root else None
        self.parent: Node = None
        self.small: Node = None
        self.big: Node = None

    def add_pre(self, anode):
        q = f"? {self.label} {anode.label}"
        print(q, flush=True)
        comp = input()
        self.add(anode, comp)

    def add(self, anode, comparator):
        if comparator == "<":
            if self.big is None:
                self.big = anode
                anode.parent = self
            else:
                big = self.big
                print(self.__repr__())
                big.add_pre(anode)
        else:
            if self.small is None:
                self.small = anode
                anode.parent = self
            else:
                print(self.__repr__())
                self.small.add_pre(anode)

    def count(self):
        count = 1
        if self.small is None and self.big is None:
            return count
        if self.small is not None:
            count += self.small.count()
        if self.big is not None:
            count += self.big.count()
        return count

    def left_count(self):
        count = 0
        if self.small is None:
            return count
        else:
            count += self.small.count()
        return count

    def right_count(self):
        count = 0
        if self.big is None:
            return count
        else:
            count += self.big.count()
        return count

    def root_rotate_left(self): # 新しいroot Nodeを返す　左回転
        if self.parent is not None:
            return self

        if self.big is None:
            return self

        new_root = self.big
        self.big = None
        if new_root.small is None:
            new_root.small = self
            new_root.parent = None
            self.parent = new_root
        else:
            self.big = new_root.small
            new_root.small = self
            new_root.parent = None
            self.parent = new_root
        return new_root

    def root_rotate_right(self): # 新しいroot Nodeを返す 右回転
        if self.parent is not None:
            return self

        if self.small is None:
            return self

        new_root = self.small
        self.small = None
        if new_root.big is None:
            new_root.big = self
            new_root.parent = None
            self.parent = new_root
        else:
            self.small = new_root.big
            new_root.big = self
            new_root.parent = None
            self.parent = new_root
        return new_root

    def result(self):
        result_str = ""
        if self.small is None:
            result_str = self.label
        else:
            result_str = result_str + self.small.result()
            result_str = result_str + self.label
        if self.big is None:
            return result_str
        else:
            result_str = result_str + self.big.result()
        return f"{result_str}"

    def get_label(self, node):
        return "-" if node is None else node.label

    def __repr__(self):
        return f"{self.label}[parent={self.get_label(self.parent)}, Small={self.small}, Big={self.big}]"


def main():
    n, q = (int(x) for x in input().split())
    nodes = []
    for i in range(n):
        nodes.append(Node(label=chr(65+i)))
    count = 1
    start = n//2
    root = nodes[start]
    while count <= start:
        new_node = nodes[start-count]
        root.add_pre(new_node)
        # print(root)
        if start + count >= n:
            break
        new_node = nodes[start+count]
        root.add_pre(new_node)
        # print(root)
        # start += 1
        count += 1
        bias = root.left_count() - root.right_count()
        # print(f"{bias=}")
        if abs(bias) > 3:
            if bias < 0:
                new_root = root.root_rotate_left()
            else:
                new_root = root.root_rotate_right()
            root = new_root
            # print(f"balanced: {root}")
    print("!", root.result(), flush=True)
    # print(f"count={count}")


if __name__=="__main__":
    main()


