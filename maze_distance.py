class position():
    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist = dist


def bfs(x, y, dist):
    global result
    queue.append(position(x, y, dist))
    visit[y][x] = True

    while queue:
        current = queue.pop(0)

        if current.x == end[0] and current.y == end[1]:
            result = current.dist-2
            break

        for i in range(4):
            next_y = current.y + direction[i][0]
            next_x = current.x + direction[i][1]
            next_dist = current.dist + 1

            if -1<next_x<width and -1< next_y < height:
                if visit[next_y][next_x] == False and maze[next_y][next_x] == 0 or visit[next_y][next_x] == False and maze[next_y][next_x] == 3:
                    visit[next_y][next_x] = True
                    queue.append(position(next_x, next_y, next_dist))


direction = ((1, 0), (-1, 0), (0, 1), (0, -1))

for t in range(int(input())):
    n = int(input())
    width = height = n
    visit = [[False] * n for _ in range(n)] # visit = [[False] * n] * n 로 하면 안됨!
    queue = []
    result = 0
    maze = [list(map(int, input())) for _ in range(n)]

    for i in range(height):
        for j in range(width):
            if maze[i][j] == 3:
                end = (j, i)
            if maze[i][j] == 2:
                start = (j, i)

    bfs(start[0], start[1], 1)
    print("#{} {}".format(t+1, result))
