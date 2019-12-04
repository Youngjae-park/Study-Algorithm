#no_zero
num = int(input())
str_num = str(num+1)

A = list(str_num)

for i in range(len(A)):
    if(A[i] == '0'):
        A[i] = '1'

print(''.join(A))
