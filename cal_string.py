#calculate from string
A = list(input())
B = list(A)

def cal():
    global num_A
    global num_B
    if(op=='+'):
        return num_A+num_B
    elif(op=='-'):
        return num_A-num_B
    elif(op=='*'):
        return num_A*num_B

idx_op = 0

for i in range(len(A)):
    if(A[i]=='+' or A[i]=='-' or A[i]=='*'):
        idx_op = i
        op = A[idx_op]

for _ in range(0,idx_op+1):
    B.pop(0)

for _ in range(idx_op,len(A)):
    A.pop()

num_A = int(''.join(A))
num_B = int(''.join(B))
print(cal())
