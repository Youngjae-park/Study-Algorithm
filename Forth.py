def oper(num1, num2, op):
    if(op=='+'): return num1+num2
    elif(op=='-'): return num1-num2
    elif(op=='*'): return num1*num2
    elif(op=='/'): return int(num1/num2)

T = int(input())

operator = ['+','-','*','/']

for test_case in range(1,T+1):
    forth = list(input().split())
    stack_num = []
    stack_op = []

    while(True):
        print(forth)
        print(stack_num)
        print(stack_op)
        if(forth[0]=='.'):
            if(len(stack_num)==1):
                print("#{0} {1}".format(test_case, stack_num.pop()))
                break
            else:
                print("#{0} error".format(test_case))
                break
        elif(forth[0] not in operator):
            stack_num.append(int(forth.pop(0)))
        elif(forth[0] in operator):
            if(len(stack_num)<2):
                #print error
                print("#{0} error".format(test_case))
                break
            else:
                num2 = stack_num.pop()
                num1 = stack_num.pop()
                stack_num.append(oper(num1, num2, forth.pop(0)))
        
