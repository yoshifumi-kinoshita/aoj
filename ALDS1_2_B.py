from sys import stdin

def selectionSort(A, N):
    sw = 0
    for i in range(0, N):
        minj = i
        for j in range(i, N):
            if A[j] < A[minj]:
                minj = j
        if A[i] != A[minj]:
            v = A[i]
            A[i] = A[minj]
            A[minj] = v
            sw = sw + 1
    return sw


def printArray(A):
    print(" ".join(map(str, A)))

n = int(stdin.readline().rstrip())
a = []
a = [ int(d) for d in stdin.readline().rstrip().split() ]

sw = selectionSort(a, n)
printArray(a)
print( sw )

