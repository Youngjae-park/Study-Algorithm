T = int(input())

class node():
    def __init__(self, v, cnt):
        self.v = v
        self.cnt = cnt

def bfs(s, g, cnt):
    global result
    current = node(s, cnt)
    queue = []
    visited = []
    visited.append(s)

    queue.append(current)
    while queue:
    
        current = queue.pop(0)
        if current.v == g:
            result = current.cnt
            break
        for i in graph[current.v]:
            if i not in visited:
                queue.append(node(i,current.cnt + 1))
                visited.append(i)
        

for test_case in range(1, T+1):
    v, e = map(int, input().split())
    graph = dict()
    result = 0 
    
    for i in range(v):
        graph[str(i+1)]=[]

    for _ in range(e):
        s, g = input().split()
        graph[s].append(g)
        graph[g].append(s)

    s, g = input().split()

    bfs(s, g, 0)
    print("#{} {}".format(test_case, result))
