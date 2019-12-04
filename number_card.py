T = int(input())

def perm(count, tmp, k, n):
    global min_
    global max_

    if k == n:
        #print(tmp)
        ans = number[0]
        for i in range(n):
            ans = op(ans, tmp[i], number[i+1])
        if ans > max_:
            max_ = ans
        if ans < min_:
            min_ = ans
    else:
        for i in range(4):
            if oper[i] - count[i] > 0:
                count[i] += 1
                tmp.append(i)
                perm(count, tmp, k+1, n)
                tmp.pop()
                count[i] -= 1
            

def op(num1, oper, num2):
    if oper == 0:
        return int(num1 + num2)
    if oper == 1:
        return int(num1 - num2)
    if oper == 2:
        return int(num1 * num2)
    if oper == 3:
        if num1*num2<0:
            return int(num1/num2)
        else:
            return int(num1/num2)



for test_case in range(1, T+1):
    N = int(input())
    oper = list(map(int, input().split()))
    number = list(map(int, input().split()))
    #print(oper)

    max_ = -10000000000
    min_ = 100000000000
    '''
    for i in range(4):
        for _ in range(oper.pop(0)):
            oper.append(i)
    '''
    n = sum(oper)
    perm([0]*4, [], 0, sum(oper))
    
    '''
    for x in oper_ch:
        print(oper)
        print(x)
        ans = number[0]
        for j in range(len(x)):
            #print(ans, end= ' ')
            ans = op(ans, x[j], number[j+1])
            print(ans, end= ' ')
        print()
        if ans > max_:
            max_ = ans
        if ans < min_:
            min_ = ans
    '''
        

    
    
    '''
    for i in range(len(oper)):
        #print(oper[i])
        ans = number[0]
        for j in range(len(number)-1):
            #if i == len(oper)-2:
                #print(ans)
            ans = op(ans,oper[i][j],number[j+1])
        #print(ans)
        if ans > max_:
            max_ = ans
        if ans < min_:
            min_ = ans
    '''     
        

        
    print("#{} {}".format(test_case, max_-min_))


        
