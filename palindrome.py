#Function for checking palindrome from Left to Right
def compare_list_LR(row, index):
    global array
    global size
    global count
    comp = list()
    for k in range(index,index+size):
        comp.append(array[row][k])
    comp2 = list(comp)
    comp2.reverse()
    if(comp == comp2):
        count = count + 1
        #print(comp)

#Function for checking palindrome from Top to Bottom
def compare_list_UD(row, index):
    global array
    global size
    global count
    comp = list()
    for k in range(index, index+size):
        comp.append(array[k][row])
    comp2 = list(comp)
    comp2.reverse()
    if(comp == comp2):
        count = count +1
        #print(comp)

for test_case in range(1,11):
    size = int(input())
    array = list()
    count = 0
    
    for _ in range(8):
        array.append(list(input()))

    for row in range(8):
        for index in range(9-size):
            compare_list_LR(row,index)
            compare_list_UD(row,index)
    print("#{0} {1}".format(test_case, count))


#Input
4
CBBCBAAB
CCCBABCB
CAAAACAB
BACCCCAC
AABCBBAC
ACAACABC
BCCBAABC
ABBBCCAA
4
BCBBCACA
BCAAACAC
ABACBCCB
AACBCBCA
ACACBAAA
ACCACCCB
AACAAABA
CACCABCB
3
BABBBACB
ABCAACCB
CCACBCBA
CACACBCA
CCABACCB
CCBAAAAA
BBACBACA
CBCCBABC
4
ACBBCCCA
CCBCBACB
ACBCABAA
BABCCAAA
ACCCCCBB
AABBCCBC
CCABBACA
CAACBCCC
7
AAACACAB
CCABCCCC
CABCAAAA
BBBCBBBA
ABCCACCC
ABACBCBB
CBABACAB
BBBBBABB
3
ABCBCBCA
ABCBCCCB
ABACCCCA
BBABBBAC
BBACBCCC
AAACACCA
BABCCCBC
ACCBCBCA
7
CACBCCBA
CBCCBCCA
CCBCBCAB
BBCCABAA
CACCBCCC
BCCACCBB
CBCCCBBC
CBACBCBC
5
BCBABCBA
CBBABABC
BCACBAAA
BBABACAB
BCBCCBAC
CBBCBBBB
CBBAACAB
ACCBCBCC
3
BBBBCCAA
BCBBCACC
BBCAAAAB
ABABBABB
BACAAABA
ABACCBCA
ACCAABCB
BACCACBA
5
BCCCACCB
CABCACAB
BAACCCAC
BBABBABC
CCABABCA
CABABACC
CBACACAB
CBCCCBAB

