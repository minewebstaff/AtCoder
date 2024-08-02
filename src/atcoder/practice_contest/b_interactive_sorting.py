class Node:
    def __init__(self, label):
        self.label = label
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
            else:
                big = self.big
                big.add_pre(anode)
        else:
            if self.small is None:
                self.small = anode
            else:
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
        count = 1
        if self.small is None:
            return count
        else:
            count += self.small.count()
        return count

    def right_count(self):
        count = 1
        if self.big is None:
            return count
        else:
            count += self.big.count()
        return count


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

    def __repr__(self):
        return f"{self.label}[Small={self.small} Big={self.big}]"


def main():
    n, q = (int(x) for x in input().split())
    nodes = []
    for i in range(n):
        nodes.append(Node(label=chr(65+i)))
    count = 0
    start = 1
    root = nodes[0]
    while start < n:
        new_node = nodes[start]
        root.add_pre(new_node)
        start += 1
        count += 1
    print("!", root.result(), flush=True)
    # print(f"count={count}")


if __name__=="__main__":
    main()


