N = int(input())

time = [-1]*(N+1)
edge = [[] for _ in range(N+1)]
indegree = [-1]*(N+1)
for i in range(1, N+1):
    info = list(map(int, input().split()))
    time[i] = info.pop(0)
    info.pop()
    indegree[i] = len(info)
    for idx_before in info:
        edge[idx_before].append(i)
    
queue = []
result = []
for i in range(1, N+1):
    if(indegree[i] == 0):
        queue.append(i)

while(queue):
    node = queue.pop(0)
    result.append(node)
    for linked_node in edge[node]:
        indegree[linked_node] -= 1
    for i in range(1, N+1):
        if(indegree[i] == 0 and i not in queue and i not in result):
            queue.append(i)

while(result):
    node = result.pop(0)
    max_ = 0
    #print("NODE : ", node)
    for i in range(1,N+1):
        if node in edge[i]:
            max_ = max(max_, time[i])
            #print(i, max_)
    time[node] += max_

for i in range(1,N+1):
    print(time[i])
