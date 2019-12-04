#Hamming distance
binaryA = list(input())
binaryB = list(input())

def hamming():
    global binaryA
    global binaryB
    length = 0

    for _ in range(len(binaryA)):
        length = length + abs(int(binaryA.pop())-int(binaryB.pop()))

    return length

if(len(binaryA)>len(binaryB)):
    difference = len(binaryA) - len(binaryB)
    for _ in range(difference):
        binaryB.insert(0,0)
elif(len(binaryB)>len(binaryA)):
    difference = len(binaryB) - len(binaryA)
    for _ in range(difference):
        binaryA.inser(0,0)

print(hamming())
