class Node:
    def __init__(self, name, h):
        self.name = name
        self.h = h
        self.children = []

def ida_star(start, goal):
    def dfs(node, g, bound, path):
        f = g + node.h
        if f > bound:
            return f
        if node.name == goal:
            return path + [node.name]
        min_bound = float('inf')
        for child, cost in node.children:
            if child.name not in path:
                res = dfs(child, g + cost, bound, path + [node.name])
                if isinstance(res, list):
                    return res
                min_bound = min(min_bound, res)
        return min_bound

    bound = start.h
    while True:
        res = dfs(start, 0, bound, [])
        if isinstance(res, list):
            return res
        if res == float('inf'):
            return None
        bound = res

# ----- Input -----
n = int(input("Nodes: "))
nodes = {}
for _ in range(n):
    name = input(f"Name of node {_ + 1}: ").strip()
    h = int(input(f"Heuristic of {name}: "))
    nodes[name] = Node(name, h)

e = int(input("Edges: "))
for _ in range(e):
    u, v, c = map(str.strip, input("Edge (from to cost): ").split())
    nodes[u].children.append((nodes[v], int(c)))

start = input("Start node: ").strip()
goal = input("Goal node: ").strip()

# ----- Run -----
path = ida_star(nodes[start], goal)
print("Path:", " -> ".join(path) if path else "No path found")