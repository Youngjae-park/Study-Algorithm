N = int(input())

info_building = [-1]

def min_time(num_building, must):
    global time
    tot = 0
    if not must:
        time[num_building] = info_building[num_building][0]
        return
    else:
        for num_must in must:
            if time[num_must] != -1:
                tot = max(tot, time[num_must])
            else:
                min_time(num_must, info_building[num_must][1])
        time[num_building] = tot + info_building[num_building][0]
        return
            

for num_building in range(N):
    temp = []
    info = list(map(int, input().split()))
    temp.append(info.pop(0))
    info.pop()
    temp.append(info)
    info_building.append(temp)

time = [-1]*(N+1)
for num_building in range(1,N+1):
    min_time(num_building, info_building[num_building][1])

for i in range(1, N+1):
    print(time[i])
