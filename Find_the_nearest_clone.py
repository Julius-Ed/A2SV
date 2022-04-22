from collections import deque


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    graph = {}
    for i in range(1, graph_nodes + 1):
        color = ids[i - 1]
        graph[i] = (color, [])

    for a, b in zip(graph_from, graph_to):
        graph[a][1].append(b)
        graph[b][1].append(a)

    colorToNode = {}
    for node, colorId in enumerate(ids):

        if colorId not in colorToNode:
            colorToNode[colorId] = [node + 1]
        else:
            colorToNode[colorId].append(node + 1)

    if val not in colorToNode:
        print(-1)
        return

    res = float('inf')
    startingNodeCandidates = colorToNode[val]

    while len(startingNodeCandidates) > 0:

        visited = set()
        candidateNode = startingNodeCandidates.pop()
        q = deque([(candidateNode, 0)])
        visited.add(candidateNode)

        while q:

            current,  pathLength = q.popleft()
            if current != candidateNode and graph[current][0] == val:
                res = min(pathLength, res)
                break

            children = graph[current][1]

            for child in children:
                if child not in visited:
                    q.append((child, pathLength + 1))
                    visited.add(child)

    print(res)


graph_nodes = 5
graph_from = [1, 1, 2, 3]
graph_to = [2, 3, 4, 5]
ids = [1, 2, 3, 3, 2]
val = 2

findShortest(graph_nodes, graph_from, graph_to, ids, val)
