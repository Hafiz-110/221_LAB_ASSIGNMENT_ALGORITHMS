import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]
g, indeg, used = defaultdict(list), defaultdict(int), set()

for i in range(n-1):
    w1, w2 = words[i], words[i+1]
    if len(w1) > len(w2) and w1.startswith(w2):
        print(-1); exit()
    for a, b in zip(w1, w2):
        if a != b:
            g[a].append(b); indeg[b] += 1
            break
for w in words: used |= set(w)

pq = [c for c in used if indeg[c]==0]
heapq.heapify(pq)
res = []
while pq:
    u = heapq.heappop(pq)
    res.append(u)
    for v in g[u]:
        indeg[v] -= 1
        if indeg[v]==0: heapq.heappush(pq, v)

print("".join(res) if len(res)==len(used) else -1)
