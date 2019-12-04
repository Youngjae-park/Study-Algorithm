T = int(input())

dec = {'0110': 0, '1100': 1, '1001': 2, '1110': 3, '0001': 4, '1000': 5, '0111': 6, '1101': 7, '1011': 8, '0101': 9}
h = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
     '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    code = set()
    prev = None
    inp = []
    for _ in range(N):
        temp = input().strip('0').split('00000')
        for i in temp:
            i = i.strip('0')
            if i not in inp:
                inp.append(i)
    for temp in inp:
        for i in code:
            temp = temp.replace(i, "")
        temp = temp.strip('0')
        code.add(temp)
    real = set()
    for cd in code:
        for i in code:
            if i!= cd:
                cd = cd.replace(i, "")
        real.add(cd)
    result = 0
    real -= {''}
    for temp in real:
        ans = ''
        for i in temp:
            ans += h[i]
        t = len(ans) - 1
        while ans[t] == "0":
            t -= 1
        ans = '0'*28 + ans[:t+1]
        t = 1
        while len(ans) >= t*56:
            t += 1
        t -= 1
        ans = ans[len(ans) - t*56]
