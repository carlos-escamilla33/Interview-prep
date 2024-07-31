
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




graph = {
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

depthFirstPrint(graph, "a")
