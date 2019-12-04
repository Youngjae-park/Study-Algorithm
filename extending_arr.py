T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    temp = []
    arr = []
    for _ in range(M):
        temp.append(list(map(int, input().split())))
    print(temp)
    arr.extend(temp.pop(0))
    while(temp):
        print(arr)
        largest = max(arr)
        cmp_arr = temp.pop(0)
        cmp_num = cmp_arr[0]
        here = len(arr)
        if(largest>cmp_arr[0]):
            for i in range(len(arr)):
                if(arr[i]>cmp_num):
                    here = i
                    break

        temp1 = arr[:here]
        temp2 = arr[here:]
        temp1.extend(cmp_arr)
        temp1.extend(temp2)
        arr = temp1[len(temp1)-11:]


    print("#{} ".format(test_case), end = "")
    for i in range(1, 11):
        print("{} ".format(arr[-i]), end = "")
    print()
