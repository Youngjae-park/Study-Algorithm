T = int(input())

class atom():
    def __init__(self, x, y, direction, K, vanish=False):
        self.x = x
        self.y = y
        self.direction = direction
        self.K = K
        #self.f_x = x + dir_[direction][0]*0.5
        #self.f_y = y + dir_[direction][1]*0.5
        self.vanish = vanish
'''
def hope(atom_A, atom_B):
    global min_dist
    if atom_A != atom_B:
        distance = abs(atom_A.x - atom_B.x) + abs(atom_A.y - atom_B.y)
        if distance != 0:
            if distance < min_dist:
                min_dist = distance
'''
def lapse(atom, n):
    dx, dy = dir_[atom.direction]
    if n == 0:
        atom.x += dx
        atom.y += dy
        #atom.f_x += dx
        #atom.f_y += dy
        return
    
    atom.x += dx*n
    atom.y += dy*n
    #atom.f_x += dx*n
    #atom.f_y += dy*n
    
def crush(atom_A, atom_B):
    global min_dist
    if atom_A != atom_B:
        distance = abs(atom_A.x - atom_B.x) + abs(atom_A.y - atom_B.y)
        if distance != 0:
            if distance < min_dist:
                min_dist = distance
                
    if atom_A == atom_B:
        return
    if atom_A.x == atom_B.x and atom_A.y == atom_B.y:
        atom_A.vanish = True
        atom_B.vanish = True
        return
    #if atom_A.f_x == atom_B.f_x and atom_A.f_y == atom_B.f_y:
    #    atom_A.vanish = True
    #    atom_B.vanish = True
    #    return

dir_ = ((0,0.5),(0,-0.5),(-0.5,0),(0.5,0))

for test_case in range(1, T+1):
    N = int(input())
    list_atom = []
    sum_E = 0
    

    for i in range(N):
        x, y, direction, K = map(int, input().split())
        list_atom.append(atom(x, y, direction, K))

    t=0
    while list_atom:
        min_dist = 4000
        #print(t, min_dist, len(list_atom))
        del_atom = []

        for t_a in list_atom:
            if t_a.x < -1000 or t_a.x > 1000 or t_a.y <-1000 or t_a.y > 1000:
                list_atom.remove(t_a)
        
        for i in range(len(list_atom)):
            for j in range(i,len(list_atom)):
                crush(list_atom[i], list_atom[j])

        k=0
        for i in range(len(list_atom)):
            #print(i, k, len(list_atom))
            if list_atom[i-k].vanish == True:
                #print("HERE", list_atom[i-k].K)
                sum_E += list_atom[i-k].K
                list_atom.pop(i-k)
                k += 1

        #time lapse
        for i in range(len(list_atom)):
            lapse(list_atom[i], min_dist//2)
            
        #print(t, min_dist, len(list_atom))            
        t += min_dist//2

    print("#{} {}".format(test_case, sum_E))
