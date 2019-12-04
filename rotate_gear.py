T = int(input())

def rotate_c(arr):
    arr.insert(0,arr.pop())
    return
def rotate_cc(arr):
    arr.insert(7,arr.pop(0))
    return

for test_case in range(1, T+1):
    K = int(input())
    gear = [list(map(int, input().split())) for _ in range(4)]
    move = [list(map(int, input().split())) for _ in range(K)]

    while move:
        num_gear, dir_c = move.pop(0) #num_gear 는 index 보다 1큼
        check_ = [0]*4

        dir_ = [0]*4
        dir_[num_gear-1] = dir_c
        next_dir_r, next_dir_l = dir_c, dir_c

        for i in range(num_gear-1,3):
            if gear[i][2] != gear[i+1][6]:
                next_dir_r = (-1)*next_dir_r
                dir_[i+1] = next_dir_r
            else:
                break
        for i in range(num_gear-1,0,-1):
            if gear[i][6] != gear[i-1][2]:
                next_dir_l = (-1)*next_dir_l
                dir_[i-1] = next_dir_l
            else:
                break
            
        #print(dir_)
        
        for i in range(4):
            if dir_[i] == 1:
                rotate_c(gear[i])
            if dir_[i] == -1:
                rotate_cc(gear[i])
    times = 0
    result = 0
    for i in range(4):
        result += gear[i][0]*(2**times)
        times += 1

    print("#{} {}".format(test_case, result))
