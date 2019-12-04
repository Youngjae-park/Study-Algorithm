T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int,input().split()))
    for _ in range(M):
        arr.append(arr.pop(0))
    print("#{} {}".format(test_case, arr[0]))
