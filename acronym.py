T = int(input())

for test_case in range(1, T+1):
    arr = list(input().split())
    result = []
    #result = list()

    for i in range(len(arr)):
        temp_char = arr[i][0]
        result.append(temp_char.upper())
        

    print("#{} ".format(test_case), end = '')
    for x in result:
        print(x, end = '')
    print()
