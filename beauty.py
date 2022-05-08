
from collections import deque


def validateCompanyStrcuture(reportingLines):

    indegree, graph = {}, {}
    allEmployees = set()
    globalVisited = set()
    res = []

    # populate graph and indegree dictionaries.
    for ele in reportingLines:
        employee, supervisor = ele.split()

        allEmployees.add(employee)
        allEmployees.add(supervisor)

        if supervisor not in graph:
            graph[supervisor] = [employee]
        else:
            graph[supervisor].append(employee)

        # indegree counts number of supervisors an employee has.
        if employee not in indegree:
            indegree[employee] = 1
        else:
            indegree[employee] += 1

    ceos = getCeos(allEmployees, indegree)

    # check whether multiple ceos exist.
    if len(ceos) > 1:
        return "Multiple CEOs found: " + ", ".join(ceos)

    # traverse the graph to detect cycles.
    for node in graph:

        # only run BFS on graph if the node has not been visited before.
        if node not in globalVisited:
            cycle, localVisited = checkCycle(node, graph)

            res += cycle
            globalVisited |= localVisited

    if len(res) == 0:
        return "The company structure is valid"
    if len(res) > 1:
        return "Multiple loops were detected"

    else:
        res.sort()
        return_string = ", ".join(res[0])
    return "A loop was detected involving: "+return_string


def getCeos(allEmployees, indegree):
    # checks whether multiple ceos exist.

    ceos = []
    for emp in allEmployees:
        if emp not in indegree:
            ceos.append(emp)

    ceos.sort()

    return ceos


def checkCycle(node, graph):
    # checks whether cycles exists. Returns node involved in a cycle.
    res = []
    visited = {node}
    startNode = (node, [])

    q = deque([startNode])

    while q:
        curr, currPath = q.popleft()

        # employee is not a supervisor,
        if curr not in graph:
            continue

        # loop through children and update path.
        for child in graph[curr]:
            childNode, childPath = (child, currPath + [curr])

            if child not in visited:
                visited.add((childNode))
                q.append((childNode, childPath))

            # if a child node has been visited, child is start of a cycle.
            else:
                cycle = []
                for index in range(len(childPath)-1, -1, -1):
                    cycle.append(childPath[index])
                    if childPath[index] == child:
                        break
                res.append(cycle)

    return res, visited


testCase1 = ["Pete Nick", "Barbara Nick", "Nick Sophie"]
testCase2 = ["Pete Nick", "Barbara Nick", "Nick Sophie",
             "Jonas Silvia"]
testCase3 = ["Pete Nick", "Barbara Nick", "Nick Sophie", "Sophie Nick"]
testCase4 = ["Pete Nick", "Barbara Nick",
             "Nick Sophie", "Julius Pete", "Nick Julius", "Solomon Barbara", "Barbara Solomon"]
testCase5 = ["Nick Sophie", "Nick Pete", "Pete Julius",
             "Barbara Nick", "Solomon Barbara", "Julius Solomon"]

for test in [testCase1, testCase2, testCase3, testCase4, testCase5]:
    print(validateCompanyStrcuture(test))
