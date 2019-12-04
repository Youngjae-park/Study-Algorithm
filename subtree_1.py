T = int(input())

for test_case in range(1, T+1):
    E, N = map(int, input().split())
    info = list(map(int, input().split()))
    tree = []

    #make tree
    while(info):
        parent = info.pop(0)
        children = info.pop(0)
        tree.append((parent, children))

    child_node=[]
    cnt = 1
    for i in range(len(tree)):
        if(tree[i][0] == N):
            child_node.append(tree[i][1])
            cnt += 1

    while(child_node):
        target_node = child_node.pop(0)
        for i in range(len(tree)):
            if(tree[i][0] == target_node):
                child_node.append(tree[i][1])
                cnt += 1

    print("#{} {}".format(test_case, cnt))
