def dfs_limited (node, depth, visited, tree):
    if depth < 0 or node in visited:
        return
    print(node, end='')
    visited.add(node)
    for neighbor in tree.get(node, []):
        dfs_limited (neighbor, depth-1, visited, tree)

def iddfs (start, tree, max_depth):
    for depth in range (max_depth+1):
            visited = set()
            print(f"\nDepth {depth}: ", end='')
            dfs_limited(start, depth, visited, tree)

n = int(input("Enter the number of nodes in tree: "))
print("Enter the edges (parent child) one per line")
tree = {}

for _ in range (n-1):
     u, v = input().split()
     tree.setdefault(u, []).append(v)
     tree.setdefault(v, []).append(u)

root = input("Enter the root node to perform IDDFS: ")
max_depth = int(input("Enter maximum depth for IDDFS: "))
print("IDDFS traversal: ")
iddfs (root, tree, max_depth)