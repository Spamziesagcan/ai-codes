class Node:
    def __init__(self, name, val):
        self.name, self.val, self.children = name, val, []

n = int(input("No. of nodes: "))
nodes = {}

# Step 1: Input node names and values
for _ in range(n):
    name = input("Node name: ")
    val = int(input(f"Value of {name}: "))
    nodes[name] = Node(name, val)

# Step 2: Input parent-child relationships
while True:
    p = input("Parent (or 'done'): ")
    if p == 'done': break
    for _ in range(int(input(f"How many children for {p}? "))):
        c = input("Child: ")
        nodes[p].children.append(nodes[c])

# Step 3: Hill climbing
start = nodes[input("Start node: ")]
path = [start.name]
while True:
    better = max((c for c in start.children if c.val > start.val), default=None, key=lambda x: x.val)
    if not better: break
    start = better
    path.append(start.name)

print("Path:", " -> ".join(path))
print("Final value:", start.val)