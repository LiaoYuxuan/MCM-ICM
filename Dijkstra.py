import math

# graph = {'a': {'b': 10, 'c': 3},
#          'b': {'d': 2, 'c': 1},
#          'c': {'b': 4, 'd': 8, 'e': 2},
#          'd': {'e': 7, },
#          'e': {'d': 9}
#          }

graph = {'a': {'b': 5, 'c': 1},
         'b': {'a': 5, 'c': 2, 'd': 1},
         'c': {'a': 1, 'b': 2, 'd': 4, 'e': 8},
         'd': {'b': 1, 'c': 4, 'e': 3, 'f': 6},
         'e': {'c': 8, 'd': 3},
         'f': {'d': 6}
         }


def dijkstra(graph, start, goal):
    # 每个点到起始点的最小距离，类似于大小为1*n的数组
    shortest_distance = {}
    # 记录祖先点
    predecessor = {}
    # 复制graph并进行点的遍历
    unseenNodes = graph
    infinity = math.inf
    # 记录路径
    path = []
    # 初始化距离
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    # 判断字典是否为空，即点是否遍历完成
    while unseenNodes:
        minNode = None
        # 第一个循环是为了比较大小，找出shortest_distance最小的结点minNode,即为下一步分析的结点
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        # 第二个循环是为了update数据，以minNode为出发点，shortest_distance[minNode]是到minNode这个
        # 结点已经走过的距离，weight是从minNode往下一个结点childNode走的距离，shortest_distance[chi
        # ldNode]是指上一轮循环中得出的从起点到childNode的距离，若本轮数值比上一轮小，则替换
        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        # minNode作为已经走过的点，在循环结束时应当pop出去
        unseenNodes.pop(minNode)

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


dijkstra(graph, 'a', 'f')