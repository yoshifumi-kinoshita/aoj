from sys import stdin
import queue

n, q = list(map(int, stdin.readline().rstrip().split()))
queue = queue.Queue()
for i in range(n):
    name, time = stdin.readline().rstrip().split()
    queue.put([name, int(time)])


past = 0
answer = []
while queue.qsize() > 0:
    name, time = queue.get()
    if time - q > 0:
        queue.put([name, time - q])
        past += q
    else:
        answer.append([name, past+time])
        past += time


for j in answer:
    print("%s %d" %(j[0], j[1]))

