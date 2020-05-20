from sys import stdin

def bubbleSort(A, N):
    flag = True
    i = 0
    j = 0
    sw = 0

    while flag:
        flag = False
        for j in range(n-1, 0, -1):
            if a[j] < a[j-1]:
                v = a[j]
                a[j] = a[j-1]
                a[j-1] = v
                sw = sw + 1
                flag = True
        i = i+1
    return sw

def printArray(A):
    print(" ".join(map(str, A)))

n = int(stdin.readline().rstrip())
a = []
a = [ int(d) for d in stdin.readline().rstrip().split() ]

sw = bubbleSort(a, n)
printArray(a)
print( sw )

