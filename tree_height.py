# 221RDB300 Daniils Ledovskojs 2. prupa

import sys
import threading
import numpy


def build_tree(n, parents):
    tree = {}
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            if parent not in tree:
                tree[parent] = []
            tree[parent].append(i)
    return tree, root


def compute_height(tree, root):
    if root not in tree:
        return 0
    height = 0
    for child in tree[root]:
        height = max(height, compute_height(tree, child))
    return height + 1




def main():
    text = input()
    if "F" in text:
        file_p = input()
        path = "test/" + file_p
        if not "a" in file_p:
            text = open(path)
            text2 = text.read()
            text.close()
            n, parents = read_input()
            tree, root = build_tree(n, parents)
            height = compute_height(tree, root)
            print(height)
    elif "I" in text:
       n, parents = read_input()
tree, root = build_tree(n, parents)
height = compute_height(tree, root)
print(height)
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
