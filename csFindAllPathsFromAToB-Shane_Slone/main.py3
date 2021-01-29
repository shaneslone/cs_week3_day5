def csFindAllPathsFromAToB(graph):
    result = []
    target = len(graph) - 1
    def inner(n, path):
        path = path.copy()
        path.append(n)
        if n == target:
            result.append(path)
        for num in graph[n]:
            inner(num, path)
    inner(0, [])
    return result

