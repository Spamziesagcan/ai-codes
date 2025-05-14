import heapq

def astar_tree(graph, start, goal, heuristic):
    open_set = [(heuristic[start], 0, start)]
    came_from = {}
    visited = set()

    while open_set:
        _, cost, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from.get(current)
            return path[::-1]

        visited.add(current)

        for neighbor, weight in graph.get(current, []):
            if neighbor in visited:
                continue
            new_cost = cost + weight
            total_cost = new_cost + heuristic.get(neighbor, float('inf'))
            heapq.heappush(open_set, (total_cost, new_cost, neighbor))
            if neighbor not in came_from:
                came_from[neighbor] = current

    return None

# -------------------- INPUT SECTION --------------------

tree = {}
n = int(input("Enter number of edges: "))
print("Enter edges in format: from to cost")
for _ in range(n):
    u, v, w = input().split()
    u, v = u.strip(), v.strip()
    w = int(w)
    tree.setdefault(u, []).append((v, w))
    # Uncomment the next line if the graph is undirected
    # tree.setdefault(v, []).append((u, w))

heuristic = {}
m = int(input("Enter number of heuristic values: "))
print("Enter heuristics in format: node value")
for _ in range(m):
    node, h = input().split()
    heuristic[node.strip()] = int(h)

start = input("Enter start node: ").strip()
goal = input("Enter goal node: ").strip()

# -------------------- RUNNING A* --------------------
path = astar_tree(tree, start, goal, heuristic)

if path:
    print("Path:", " -> ".join(path))
else:
    print("Path: No path found")