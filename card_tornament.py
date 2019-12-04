T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    torna = list(map(int,input().split()))
    torna_token = [True]*N

    torna_a = torna[:len(torna)//2]
    torna_b = torna[len(torna)//2:]
