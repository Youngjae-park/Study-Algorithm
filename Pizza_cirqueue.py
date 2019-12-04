T = int(input())

class info():
    def __init__(self, real_idx, cheeze):
        self.real_idx = real_idx
        self.cheeze = cheeze

def pizza(N, cir_Ci):
    cir = []
    for i in range(N):
        cir.append(cir_Ci.pop(0))

    #for a in cir:
    #    print(a.real_idx, a.cheeze, end=' / ')

    while cir:
        #for a in cir:
        #    print(a.real_idx, a.cheeze, end=' / ')
            
        if(len(cir) == 1):
            break
        current = cir.pop(0)
        current.cheeze = current.cheeze//2
        if current.cheeze == 0 :
            if len(cir_Ci) != 0:
                cir.append(cir_Ci.pop(0))
                #print("!")
        else:
            cir.append(current)
            #print(end = " -> ")

    current = cir.pop(0)
    return current.real_idx + 1


for test_case in range(1, T+1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    cir_Ci = []

    for i in range(M):
        cir_Ci.append(info(i,Ci[i]))

    #for a in cir_Ci:
    #    print(a.real_idx, a.cheeze, end=' / ')

    print("#{} {}".format(test_case, pizza(N, cir_Ci)))
