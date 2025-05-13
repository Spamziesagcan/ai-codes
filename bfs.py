from collections import deque

def bfs(start, tree):
    visited = set()
    queue = deque([start])
    visited.add(start)  # Mark as visited when enqueuing

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in tree.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Input number of nodes
n = int(input("Enter number of nodes in the tree: "))
print("Enter the edges (parent child) one per line:")
tree = {}

# Build adjacency list
for _ in range(n - 1):
    u, v = input().split()
    tree.setdefault(u, []).append(v)
    tree.setdefault(v, []).append(u)  # Since it's an undirected tree

# Input root and run BFS
root = input("Enter the root node to start BFS: ")
print("BFS traversal:")
bfs(root, tree)