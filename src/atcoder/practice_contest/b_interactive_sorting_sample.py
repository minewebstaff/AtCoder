import b_interactive_sorting as b

n = 3
nodes = []
for i in range(n):
    nodes.append(b.Node(label=chr(65+i)))

count = 0
start = 1
root = nodes[0]

while start < n:
    new_node = nodes[start]
    root.add_pre(new_node)
    print(root)
    start += 1
    count += 1