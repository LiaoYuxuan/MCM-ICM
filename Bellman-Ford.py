import math

graph = {'S': {'E': 8, 'A': 10},
         'A': {'C': 2},
         'B': {'A': 1},
         'C': {'B': -2},
         'D': {'C': -1, 'A': -4},
         'E': {'D': 1}
         }


def bellman_ford(graph, start, goal):
    shortest_distance = {}
    predecessor = {}
    infinity = math.inf
    path = []

    for node in graph:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    #结点数-1是循环的最高上界
    for iteration in range(1, graph.__len__()):
        # flag用于检测距离是否发生变化，若都不变，则可以提前结束循环
        flag = 0
        # print(iteration)
        for node in graph:
            for childNode, weight in graph[node].items():
                if weight + shortest_distance[node] < shortest_distance[childNode]:
                    shortest_distance[childNode] = weight + shortest_distance[node]
                    predecessor[childNode] = node
                    # 表明距离发生了变化
                    flag = 1
        print(shortest_distance)
        if flag == 0:
            break

    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0, start)
    if shortest_distance[goal] != infinity:
        print('Every node shortest distance to ' + start + ' is ' + str(shortest_distance))
        print(goal + ' shortest distance to ' + start + ' is ' + str(shortest_distance[goal]))
        print('And the path is ' + str(path))


bellman_ford(graph, 'S', 'C')
