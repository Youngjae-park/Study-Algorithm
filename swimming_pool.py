T = int(input())

def solve(idx, plan, sum_):
    global min_
    if idx == 12:
        for i in range(12):
            if plan_day[i]:
                if plan[i] == 0:
                    #print("HERE")
                    return
        #print("here", idx, plan, sum_)
        if sum_ <min_:
            min_ = sum_

        
    else:
        for c in range(5):
            if c<3:
                if idx<12:
                    plan.append(c)
                    if c == 0:
                        solve(idx+1, plan, sum_)
                    if c == 1:
                        solve(idx+1, plan, sum_+plan_day[idx]*price[1])
                    if c == 2:
                        solve(idx+1, plan, sum_+price[2])
                    plan.pop()
            elif c==3:
                if idx<10:
                    for _ in range(3):
                        plan.append(c)
                    solve(idx+3, plan, sum_+price[3])
                    for _ in range(3):
                        plan.pop()
            elif c==4:
                if idx == 0:
                    for _ in range(12):
                        plan.append(c)
                    solve(idx+12, plan, sum_+price[4])
                    for _ in range(12):
                        plan.pop()
                else:
                    return
                

for test_case in range(1, T+1):
    price = list(map(int, input().split()))
    price.insert(0,0)
    plan_day = list(map(int, input().split()))
    min_ = 999999

    solve(0, [], 0)

    print("#{} {}".format(test_case, min_))
