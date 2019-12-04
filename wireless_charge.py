import copy
T = int(input())

#AP class
class AP():
    def __init__(self, x, y, C, P, AP_num):
        self.x = x
        self.y = y
        self.C = C
        self.P = P
        self.AP_num = AP_num

#human class
class human():
    def __init__(self, x, y, sum_charge):
        self.x = x
        self.y = y
        self.sum_charge = sum_charge

#calculate distance
def distance(a_x, a_y, b_x, b_y):
    return abs(a_x-b_x)+abs(a_y-b_y)

def charge(A, B, A_num, B_num):
    temp_A = A[1:]
    temp_B = B[1:]
    temp_A_num = A_num[1:]
    temp_B_num = B_num[1:]

    list_A = []
    list_B = []

    for i in range(len(temp_A)):
        temp = (temp_A[i], temp_A_num[i])
        list_A.append(temp)
    for i in range(len(temp_B)):
        temp = (temp_B[i], temp_B_num[i])
        list_B.append(temp)

    list_A.sort(reverse=True)
    list_B.sort(reverse=True)

    for _ in range(2):
        list_A.append((0,0))
        list_B.append((0,0))

    max_ = 0
    list_sum = []
    for i, j in ((0,0), (0,1), (1,0)):
        if i == 0 and j == 0:
            if list_A[0][1] == list_B[0][1]:
                list_sum.append(list_A[0][0]//2 + list_B[0][0]//2)
            else:
                list_sum.append(list_A[0][0] + list_B[0][0])
        else:
            list_sum.append(list_A[i][0] + list_B[j][0])
    #print(list_sum)
            
        
            
    

    return (max(list_sum), 0)

    

    
        
    

dir_ = ((0,0),(-1,0),(0,1),(1,0),(0,-1))

#main function
for test_case in range(1, T+1):
    M, A = map(int, input().split())
    move_A = list(map(int, input().split()))
    move_B = list(map(int, input().split()))
    info_AP = []
    t_map = [[[0]]*10 for _ in range(10)]
    
    #get info about AP
    for i in range(A):
        x, y, C, P = map(int, input().split())
        temp = AP(x,y,C,P,i)
        info_AP.append(temp)

    #initalize t_map
    for i in range(10):
        for j in range(10):
            t_map[i][j] = AP(j+1, i+1, 0, [0], [100])

    #draw map with information of AP
    for target_AP in info_AP:
        x, y = (target_AP.x, target_AP.y)
        for i in range(10):
            for j in range(10):
                m_x, m_y = (j+1, i+1)
                dist = distance(x, y, m_x, m_y)
                #print(dist, end="=>")
                if dist < target_AP.C + 1:
                    if target_AP.P not in t_map[i][j].P:
                        t_map[i][j].P.append(target_AP.P)
                        t_map[i][j].AP_num.append(target_AP.AP_num)
                #print(t_map[i][j].x, t_map[i][j].y, t_map[i][j].C, t_map[i][j].P, end=',')
            #print()
        #print("next_AP")
    
    #initialize human
    human_A = human(1,1,0)
    human_B = human(10,10,0)

    A_P = t_map[human_A.y-1][human_A.x-1].P
    A_AP_num = t_map[human_A.y-1][human_A.x-1].AP_num
    B_P = t_map[human_B.y-1][human_B.x-1].P
    B_AP_num = t_map[human_B.y-1][human_B.x-1].AP_num
    #print(A_P, B_P)
    sum_A_P, sum_B_P = charge(A_P, B_P, A_AP_num, B_AP_num)
    human_A.sum_charge += sum_A_P
    human_B.sum_charge += sum_B_P
    #print("t=>0", sum_A_P, sum_B_P)
    #print("t=>0", sum_A_P, sum_B_P,) #(human_A.x, human_A.y), (human_B.x, human_B.y))

    t=1
    for _ in range(M):
        A_dx, A_dy = dir_[move_A.pop(0)]
        B_dx, B_dy = dir_[move_B.pop(0)]

        if -1 < human_A.x + A_dy - 1 < 10 and -1 < human_A.y + A_dx - 1 < 10:
            human_A.x, human_A.y = t_map[human_A.y-1+A_dx][human_A.x-1+A_dy].x, t_map[human_A.y-1+A_dx][human_A.x-1+A_dy].y
        if -1 < human_B.x + B_dy - 1< 10 and -1 < human_B.y + B_dx -1 < 10:
            human_B.x, human_B.y = t_map[human_B.y-1+B_dx][human_B.x-1+B_dy].x, t_map[human_B.y-1+B_dx][human_B.x-1+B_dy].y
            

        
        A_P = t_map[human_A.y-1][human_A.x-1].P
        A_AP_num = t_map[human_A.y-1][human_A.x-1].AP_num
        B_P = t_map[human_B.y-1][human_B.x-1].P
        B_AP_num = t_map[human_B.y-1][human_B.x-1].AP_num

        #print("num", A_AP_num, B_AP_num)
        #print("AP", A_P, B_P)
        sum_A_P, sum_B_P = charge(A_P, B_P, A_AP_num, B_AP_num)
        human_A.sum_charge += sum_A_P
        human_B.sum_charge += sum_B_P
        #print("t=>{}".format(t), sum_A_P, sum_B_P, (human_A.x, human_A.y), (human_B.x, human_B.y))
        t +=1

    print("#{} {}".format(test_case, human_A.sum_charge + human_B.sum_charge))








'''
first, get info about AP
second, draw map with information of AP
## make function to calculate distance
third, make loop to follow time(t)

'''
'''input
1
20 3
2 2 3 2 2 2 2 3 3 4 4 3 2 2 3 3 3 2 2 3
4 4 1 4 4 1 4 4 1 1 1 4 1 4 3 3 3 3 3 3
4 4 1 100
7 10 3 40
6 3 2 70
'''
'''
같은 클래스가 서로다르게 선언되어도 리스트가 공유될수도있다. 정확한 이유 알아보기
'''
