# find the number of connected graph components of a miltigraph

graph = [
    [], # the index of the nodes has to start from 1 because we will use that value later
    [2, 4],
    [1, 3],
    [2, 5],
    [1, 5, 6],
    [3, 4],
    [4],
    [8],
    [7, 9],
    [8],
    [11],
    [10]
]
visited = [] # visited nodes


def dfs(x):
    for v in graph[x]:
        if v not in visited:
            visited.append(v)
            dfs(v)


def get_components():
    comps = 0
    # check every node, if not visited (seen for the first time) add to visited and BFS it
    for i in range(1, len(graph)): # that's why we have to start from 1 instead of 0
        if i not in visited:
            visited.append(i)
            comps += 1 # if not seen before that means that no previous node is connected to it
            dfs(i)

    return comps
