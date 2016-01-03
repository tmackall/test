#!/usr/bin/python


def dfs_r(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for vertex in graph[start] - visited:
        return dfs_r(graph, vertex, visited)
    return visited

def dfs_i(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

def dfs_paths_i(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        print 'vertex: %s, path: %s' % (vertex, path)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

if __name__ == '__main__':

    graph = {'A': set(['B', 'C']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A', 'F']),
             'D': set(['B']),
             'E': set(['B', 'F']),
             'F': set(['C', 'E'])}

#    print dfs_i(graph, 'A') # set(['A', 'C', 'B', 'E', 'D', 'F'])
#    print dfs_r(graph, 'A') # set(['A', 'C', 'B', 'E', 'D', 'F'])
    print list(dfs_paths_i(graph, 'A', 'F'))
