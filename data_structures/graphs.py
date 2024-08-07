
def depthFirstPrint(graph, source):
    stack = [source]

    while stack:
        curr = stack.pop()
        print(curr)
        for neighbor in graph[curr]:
            stack.append(neighbor)
        

def depthFirstPrintRecursive(graph, source):
    print(source)
    for neighbor in graph[source]:
        depthFirstPrint(graph, neighbor)

def breadthFirstPrint(graph, source):
    queue = [source]

    while queue:
        curr = queue.pop(0)
        print(curr)
        for neighbor in graph[curr]:
            queue.append(neighbor)

# def hasPath(graph, src, dst):
#     stack = [src]
#     seen = set(src)

#     while stack:
#         curr = stack.pop()
#         if curr == dst:
#             return True
#         for neighbor in graph[curr]:
#             if neighbor not in seen:
#                 stack.append(neighbor)
#             seen.add(neighbor)       
    
#     return False

def hasPathRecursive(graph, src, dst):
    if src == dst:
        return True
    for neighbor in graph[src]:
        if hasPathRecursive(graph, neighbor, dst):
            return True
    return False

def hashPathBFS(graph, src, dst):
    queue = [src]

    while queue:
        curr = queue.pop(0)
        if curr == dst:
            return True
        for neighbor in graph[curr]:
            queue.append(neighbor)
    
    return True



graph = {
    "f": ["g", "i"],
    "g": ["h"],
    "h": [],
    "i": ["g", "k"],
    "j": ["i"],
    "k": []
}



# depthFirstPrint(graph, "a")

# print(hasPathRecursive(graph, "f", "k"))
# print(hashPathBFS(graph, "f", "k")


# -----------------------

def buildGraph(edges):
    graph = {}

    for edge in edges:
        a, b = edge

        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        
        graph[a].append(b)
        graph[b].append(a)

    return graph

def hasPath(graph, src, dst, visited):
    if src == dst:
        return True
    if src in visited:
        return False
    
    visited.add(src)
    
    for neighbor in graph[src]:
        if hasPath(graph, neighbor, dst, visited):
            return True
        
    return False

def underectedGraph(edges, nodeA, nodeB):
    graph = buildGraph(edges)

    return hasPath(graph, nodeA, nodeB, set())



edges = [
    ["i", "j"],
    ["k", "j"],
    ["m", "k"],
    ["k", "l"],
    ["o", "n"]
]

# print(underectedGraph(edges, "i", "l"))

# ----------------------

def connectedComponentsCount(graph):
    visited = set()
    count = 0

    for node in graph:
        if explore(graph, node, visited):
            count += 1
    
    return count

def explore(graph, curr, visited):
    if curr in visited:
        return False
    
    visited.add(curr)

    for neighbor in graph[curr]:
        explore(graph, neighbor, visited)

    return True

# ------------------------

def largestComponent(graph):
    longest = 0
    visited = set()
    for node in graph:
        size = exploreSize(graph, node, visited)
        longest = max(longest, size)
    return longest

def exploreSize(graph, node, visited):
    if node in visited:
        return 0
    
    visited.add(node)
    size = 1
    
    for neighbor in graph[node]:
        size += exploreSize(graph, neighbor, visited)

    return size


# -----------------------
def islandCount(grid):
    visited = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            explore(grid, r, c, visited)

def explore(grid, r, c, visited):
    rowInBounds = 0 <= r and r < len(grid[0])
    colInBounds = 0 <= c and c < len(grid[0])

    if rowInBounds or colInBounds:
        return False
    
    if grid[r][c] == "W":
        return False

    pos = r + "," + c
    if pos in visited:
        return False
    visited.add(pos)


    





































