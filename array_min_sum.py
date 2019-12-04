T = int(input())

def minsum_arr(idx, cnt, visit, sum_):
    global minimum
    global arr
    if sum_>minimum:
        return
    if cnt>=idx:
        minimum = min(minimum, sum_)
        return
    for i in range(idx):
        if visit[i] == 1:
            continue
        else:
            visit[i] = 1
            minsum_arr(idx, cnt+1, visit, sum_ + arr[cnt][i])
            visit[i] = 0

for test_case in range(1, T+1):
    N = int(input())
    arr = [[]]*N
    minimum = 10000
    visit = [0]*N
    make = [0]*N

    for i in range(N):
        arr[i] = list(map(int,input().split()))

    minsum_arr(N,0,visit, 0)
    print("#{} {}".format(test_case, minimum))
