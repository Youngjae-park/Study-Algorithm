T = int(input())

for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(M):
        idx, val = map(int, input().split())
        arr.insert(idx, val)

    print("#{} {}".format(test_case, arr[L]))
