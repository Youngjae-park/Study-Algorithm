'''
T = int(input())

for test_case in range(1, T+1):
    
'''

test = int(input())
for testCase in range(test):
    row = [1, 1]
    size = int(input())
    print('#{}'.format(testCase+1))
    if size == 1:
        print('1')
    elif size == 2:
        print('1\n1 1')
    else:
        print('1\n1 1')
        # 층 생성
        tmp = [1]
        for h in range(size-2):
            for i in range(len(row) - 1):
                a = row[i] + row[i + 1]
                tmp.append(a)
            tmp.append(1)
            #출력
            for i in range(len(tmp)):
                print('{} '.format(tmp[i]), end='')
            print()
            #다음 행을 만들기 위해 정리
            restart = [1]
            row = tmp.copy()
            tmp = restart.copy()

