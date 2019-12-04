T = int(input())

class node1():
    def __init__(self, node, cnt):
        self.node = node
        self.cnt = cnt

def subtree(node, cnt):
    sub = node1(node, cnt)
    queue = []
    global visited

    queue.append(sub)

    while queue:
        current = queue.pop(0)
        visited.append(current.node)
        for i in graph[current.node]:
            if i not in visited:
                new_cnt = current.cnt + 1
                queue.append(node1(i, new_cnt))
        
    

for test_case in range(1, T+1):
    E, N = map(int, input().split())
    graph = dict()
    result = 0
    visited = []

    for i in range(1, E+2):
        graph[str(i)]=[]

    edge = list(input().split())
    for i in range(E):
        graph[edge[i*2]].append(edge[2*i+1])

    subtree(str(N), 0)
    print("#{} {}".format(test_case, len(visited)))

    
