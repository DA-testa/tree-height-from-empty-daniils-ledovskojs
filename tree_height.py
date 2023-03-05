# 221RDB300 Daniils Ledovskojs 2. prupa

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    max_height = 0
    for v in range(n):
        h = 0
        c = v
        while c != -1:
            h += 1
            c = parents[c]
        max_height = max(max_height, h)    
    return max_height


def main():
    # implement input form keyboard and from files
    text = input()
    if "F" in text:
        file_p = input()
        path = "test/" + file_p
        if not "a" in file_p:
            text = open(path)
            text2 = text.read()
            text.close()
            sep = text2.partition("\n")
            n = int(sep[0])
            parents_1 = sep[2].split(" ")
            parents = ([int(x) for x in parents_1])
            print(compute_height(n, parents))
    elif "I" in text:
        n = int(input())
        parents = list(map(int, input().split()))
        print(compute_height(n, parents))
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
