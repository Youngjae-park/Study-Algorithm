T = int(input())

class Node():
    def __init__(self, node, cnt=None):
        self.node = node
        self.cnt = cnt

def bfs(graph, start, cnt):
    global result
    visit.append(start)
    queue = [Node(start, cnt)]
    while queue:
        current = queue.pop(0)
        if current.node == g:
            result = current.cnt
            break
        for i in graph[current.node]:
            if i not in visit:
                new_cnt = current.cnt + 1
                queue.append(Node(i, new_cnt))
                visit.append(i)

for test_case in range(1,T+1):
    graph = dict()
    v, e = list(map(int, input().split()))
    result = 0
    visit = []

    #graph initialize
    for i in range(v):
        graph[str(i+1)] = []

    #Links alocated by input value
    for _ in range(e):
        key, val = input().split()
        graph[key].append(val)
        graph[val].append(key)

    s, g = input().split()

    bfs(graph, s, 0)
    print("#{} {}".format(test_case, result))
    
