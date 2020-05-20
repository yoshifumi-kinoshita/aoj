from sys import stdin
import copy

def strcmp(s1, s2):
    #return (s1 > s2) - (s1 < s2)
    return (s1[1] > s2[1]) - (s1[1] < s2[1])

def BubbleSort(C, N):
    for i in range(0, N):
        for j in range(i+1, N)[::-1]:
            if strcmp(C[j], C[j-1]) < 0:
                v = C[j]
                C[j] = C[j-1]
                C[j-1] = v

def SelectionSort(C, N):
    for i in range(0, N):
        minj = i
        for j in range(i, N):
            if strcmp(C[j], C[minj]) < 0:
                minj = j
        v = C[i]
        C[i] = C[minj]
        C[minj] = v



def printArray(A):
    print(" ".join(map(str, A)))

n = int(stdin.readline().rstrip())
a = []
a = stdin.readline().rstrip().split()
b = copy.copy(a)

BubbleSort(a, n)
SelectionSort(b, n)
printArray(a)
print("Stable")
printArray(b)
if a == b:
    print("Stable")
else:
    print("Not stable")

