T = int(input())

def sum_node(n):
    global graph
    if(n!=1):
        root = n//2
        left = root*2
        right = root*2+1
        if(right<=N):
            graph[root] = graph[left]+graph[right]
            return
        if(left<=N):
            graph[root] = graph[left]
            return
    else:
        return

for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    graph = [0]*N
    graph.insert(0, -1)
    for node_idx in range(M):
        num_leaf, leaf_val = map(int, input().split())
        graph[num_leaf] = leaf_val
    for idx in range(N, 1, -1):
        sum_node(idx)

    #print(graph)
    print("#{} {}".format(test_case, graph[L]))
