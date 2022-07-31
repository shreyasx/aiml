graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['G'],
    'D': [],
    'E': ['F'],
    'G': [],
    'F': []
}


def iterativeDDFS(curnode, dnode, graph, maxd):
    for i in range(maxd):
        if DFS(curnode, dnode, graph, i):
            return True


def DFS(curnode, dnode, graph, maxd):
    print("Checking for goal node ", curnode)
    if curnode == dnode:
        return True
    if maxd <= 0:
        return False
    for node in graph[curnode]:
        if DFS(node, dnode, graph, maxd-1):
            return True
    return False


if iterativeDDFS('A', 'F', graph, 4):
    print("Path exists")
else:
    print("Path doesnot exists")
