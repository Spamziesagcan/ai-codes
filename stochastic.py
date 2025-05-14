import random

class Node:
    def __init__(self, name, val): self.name, self.val, self.children = name, val, []

def build_tree():
    nodes = {}
    for _ in range(int(input("Nodes: "))):
        n = input("Name: "); v = int(input("Value: "))
        nodes[n] = Node(n, v)
    while True:
        p = input("Parent (type 'done' to finish): ")
        if p == "done": break
        nodes[p].children += [nodes[input("Child: ")] for _ in range(int(input("How many children? ")))]
    return nodes

def stochastic_hill(start, goal):
    curr = start
    print("Path:", curr.name, end="")
    while True:
        if curr.name == goal:
            print("\nReached goal:", curr.name)
            return
        better = [c for c in curr.children if c.val > curr.val]
        if not better:
            print("\nStuck at", curr.name)
            return
        curr = random.choice(better)
        print("->", curr.name, end="")

nodes = build_tree()
s, g = input("Start: "), input("Goal: ")
stochastic_hill(nodes[s], nodes[g])