import sys
sys.setrecursionlimit(1000000)

def dfs(node, visited, tree):
    print(node, end=' ')
    visited.add(node)
    for neighbor in tree.get(node, []):
        if neighbor not in visited:
            dfs(neighbor, visited, tree)

n = int(input("Enter number of nodes in the tree: "))
print("Enter the edges (parent child) one per line:")
tree = {}

for _ in range (n-1):
    node,neighbor = input().split()
    tree.setdefault(node,[]).append(neighbor)
    tree.setdefault(neighbor,[]).append(node)

root = input("Enter the root node to start DFS: ")
print("DFS traversal:")
dfs(root, set(), tree)