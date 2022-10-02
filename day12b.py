from collections import defaultdict


def dfs(visited, graph, node):
    res = []
    new_visit = visited + [node]

    if node == 'end':
        return [new_visit]

    for n in graph[node]:
        if n != 'start':
            if n.isupper():
                temp_res = dfs(new_visit, graph, n)
                res.extend(temp_res)
            else:
                l_case = [i for i in new_visit if i.islower()]
                twice = any([True for i in l_case if l_case.count(i) > 1])
                if (twice and new_visit.count(n) < 1) or (not twice and new_visit.count(n) < 2):
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