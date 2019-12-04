T = int(input())

def heapify(n):
    if(n==1):
        return
    root = n//2
    left = root*2
    right = root*2 + 1
    min_ = root
    if(left<=n):
        if(tree[root]>tree[left]):
            min_ = left
    if(right<=n):
        if(tree[min_]>tree[right]):
            min_ = right
    print(min_, n, tree)
    tree[min_], tree[root] = tree[root], tree[min_]
    heapify(n//2)
        

def cal(n):
    global sum_
    if(n==1):
        return
    else:
        sum_ += tree[n//2]
        cal(n//2)

for test_case in range(1, T+1):
    N = int(input())
    queue = list(map(int, input().split()))
    tree = [-1]
    idx = last_idx = 1
    sum_ = 0
    while(queue):
        tree.append(queue.pop(0))
        heapify(idx)
        idx += 1

    cal(N)
    print("#{} {}".format(test_case, sum_))
