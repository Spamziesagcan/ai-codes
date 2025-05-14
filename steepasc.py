class Node:
    def __init__(self, name, h):
        self.name = name
        self.h = h
        self.children = []

def goal_reachable(node, goal, visited=None):
    if visited is None: visited = set()
    if node.name == goal: return True
    visited.add(node.name)
    return any(goal_reachable(c, goal, visited) for c in node.children if c.name not in visited)

# Input nodes
n = int(input("Number of nodes: "))
nodes = {input("Node name: "): Node(name := input(), int(input(f"Heuristic of {name}: "))) for _ in range(n)}

# Build tree
while True:
    parent = input("Enter parent node (or 'done'): ")
    if parent == 'done': break
    if parent not in nodes: print(f"'{parent}' not defined."); continue
    for child in input(f"Children of {parent} (space-separated): ").split():
        if child in nodes: nodes[parent].children.append(nodes[child])
        else: print(f"'{child}' not defined.")

# Hill Climbing
start, goal = input("Start node: "), input("Goal node: ")
if start not in nodes or goal not in nodes:
    print("Start or goal node not defined.")
else:
    current, path = nodes[start], [start]
    while current.name != goal:
        reachable = [c for c in current.children if goal_reachable(c, goal)]
        if not reachable: print("No path to goal. Stuck at", current.name); break
        next_node = min(reachable, key=lambda x: x.h)
        if next_node.h >= current.h: print("Local minima at", current.name); break
        current = next_node
        path.append(current.name)
    print("Path:", " -> ".join(path))