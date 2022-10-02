from collections import defaultdict


def dfs(visited, graph, node):
    res = []
    new_visit = visited + [node]
    if node == 'end':
        return [new_visit]

    for n in graph[node]:
        if n != 'start':
            if n not in visited or n.isupper():
                temp_res = dfs(new_visit, graph, n)
                res.extend(temp_res)
    
    return res


if __name__ == "__main__":
    f = open('day12').read().strip().split('\n')
    graph = defaultdict(list)
    visited = []
    for x in f:
        k, v = x.split('-')
        graph[k].append(v)
        graph[v].append(k)

    print(len(dfs(visited, graph, 'start')))