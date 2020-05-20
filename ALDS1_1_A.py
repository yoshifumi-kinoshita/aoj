#!/usr/local/bin/python3

from sys import stdin

# for i = 1 to A.length-1
#     key = A[i]
#     /* insert A[i] into the sorted sequence A[0,...,j-1] */
#     j = i - 1
#     while j >= 0 and A[j] > key
#         A[j+1] = A[j]
#         j--
#     A[j+1] = key


N=int(input())
A = list(map(int, stdin.readline().rstrip().split()))

def printArray(a):
    print(' '.join([str(i) for i in a]))

printArray(A)

for i in range(1, N):
    key = A[i]
    j = i - 1
    while j >=0 and A[j] > key:
        A[j+1] = A[j]
        j -= 1
    A[j+1] = key
    printArray(A)



