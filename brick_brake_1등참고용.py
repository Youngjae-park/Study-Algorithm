def recursive(org_box, idx, org_count):
    global result
    if not result : return
    if idx == N or not org_count:
        result = min(result, org_count)
        return
 
    for w in range(W):
        box = [b[:] for b in org_box]
        stack = list()
        count = org_count
        for h in range(H):
            if box[h][w]:
                stack.append((h, w, box[h][w]))
                box[h][w] = 0
                count -= 1
                break
        if not stack: continue
        while stack:
            y, x, length = stack.pop()
            for l in range(1, length):
                for n, m in (1, 0), (0, 1), (-1, 0), (0, -1):
                    if 0 <= y + n * l < H and 0 <= x + m * l < W and box[y + n * l][x + m * l]:
                        if box[y + n * l][x + m * l] != 1:
                            stack.append((y + n * l, x + m * l, box[y + n * l][x + m * l]))
                        box[y + n * l][x + m * l] = 0
                        count -= 1
        # 맨 밑으로 내리기
        for x in range(W):
            prev = H
            for h in range(H - 1, -1, -1):
                if box[h][x]:
                    if prev - 1 != h: box[prev - 1][x], box[h][x] = box[h][x], box[prev - 1][x]
                    prev -= 1
                else:
                    continue
        recursive(box, idx + 1, count)
 
 
T = int(input())
for t in range(T) :
    N,W,H = map(int,input().split()) # W는 가로, H는 세로
    org_box = [list(map(int,input().split())) for _ in range(H)]
    org_count = sum(True for line in org_box for e in line if e)
    result = org_count+1
    recursive(org_box, 0, org_count)
    print(f"#{t+1} {result}")
