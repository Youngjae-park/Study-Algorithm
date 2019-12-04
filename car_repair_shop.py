#import timeit

#start_time = timeit.default_timer()

T = int(input())

class state():
    def __init__(self, state, left_time, customer=None):
        self.state = state
        self.left_time = left_time
        self.customer = customer
        
class customer():
    def __init__(self, num_K, num_reception, num_repair, arrival_time):
        self.num_K = num_K
        self.num_reception = num_reception
        self.num_repair = num_repair
        self.arrival_time = arrival_time

for test_case in range(1, T+1):
    N, M, K, A, B = map(int,input().split())
    arr_a = list(map(int, input().split())) # 접수 창구의 처리 시간
    arr_b = list(map(int, input().split())) # 정비 창구의 처리 시간
    arr_t = list(map(int, input().split())) # 고객의 도착시간
    
    reception = [state(False, 0)]*N
    repair = [state(False, 0)]*M
    time = 0
    current_time = 0
    result = 0

    queue_reception = []
    queue_repair = []
    queue_result = []

    for i in range(K):
        queue_reception.append(customer(i+1, 0, 0, arr_t[i]))

    ''' 
    for x in queue_reception:
        print(x.num_K, x.arrival_time)
    '''

    
    while len(queue_result) != K:
        #reception 배치
        cnt = 0
        while(cnt<len(reception) and queue_reception):
            if queue_reception[0].arrival_time <= current_time:
                for i in range(len(reception)):
                    if reception[i].state == False:
                        queue_reception[0].num_reception = i+1
                        reception[i] = state(True, arr_a[i], queue_reception.pop(0))
                        break
            cnt += 1

        #repair 배치
        cnt = 0
        while(cnt<len(repair) and queue_repair):
            for i in range(len(repair)):
                if repair[i].state == False:
                    queue_repair[0].num_repair = i+1
                    repair[i] = state(True, arr_b[i], queue_repair.pop(0))
                    break
            cnt += 1

        #reception -> queue_repair
        for i in range(N):
            reception[i].left_time -= 1
            if reception[i].left_time < 1 and reception[i].state == True:
                reception[i].state = False
                queue_repair.append(reception[i].customer)
                reception[i] = state(False, 0)

        for i in range(M):
            repair[i].left_time -= 1
            if repair[i].left_time < 1 and repair[i].state == True:
                repair[i].state = False
                queue_result.append(repair[i].customer)
                repair[i] = state(False, 0)

        #####break #한 회만 돌리고 싶을 때


        ''' 
        #남은 시간 표현
        print("current time : ", current_time)
        print("reception_left_time", end = " => ")
        for a in reception:
            if a.customer != None:
                print(a.customer.num_K, end='->')
            else:
                print("X", end='->')
            print(a.left_time, end=' / ')
        print("repair_left_time", end = " => ")
        for b in repair:
            if b.customer != None:
                print(b.customer.num_K, end='->')
            else:
                print("X", end='->')
            print(b.left_time, end=' / ')

        print()
        for a in queue_reception:
            print(a.num_K, end=',')
        print()
        for b in queue_repair:
            print(b.num_K, end=',')
        print()
        for c in queue_result:
            print(c.num_K, end=',')
        print()
        '''


        #시간 1초 추가
        current_time += 1

                

    for x in queue_result:
        if x.num_reception == A and x.num_repair == B:
            result += x.num_K
        
    if result != 0:
        print("#{} {}".format(test_case, result))
    else:
        print("#{} {}".format(test_case, -1))

#stop_time = timeit.default_timer()
#print(stop_time - start_time)

'''input
1
2 2 6 1 2
3 2
4 2
0 0 1 2 3 4
'''
