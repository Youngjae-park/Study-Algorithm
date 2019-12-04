T = int(input())

def inorder(n, last):
    global cnt
    if n<= last:
        inorder(n*2, last)
        tree[n] = cnt
        cnt += 1
        inorder(n*2+1, last)

for test_case in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)
    cnt = 1
    inorder(1, N)
    #print(tree)
    print("#{} {} {}".format(test_case, tree[N], tree[N//2]))
