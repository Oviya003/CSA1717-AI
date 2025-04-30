import heapq
goal = [[1,2,3],[4,5,6],[7,8,0]]
dirs = [(-1,0),(1,0),(0,-1),(0,1)]
def h(s): return sum(abs((v-1)//3 - i) + abs((v-1)%3 - j) for i,row in enumerate(s) for j,v in enumerate(row) if v)
def find0(s):
    for i in range(3):
        for j in range(3):
            if s[i][j]==0: return i,j
def gen(s):
    i,j = find0(s)
    for dx,dy in dirs:
        ni,nj = i+dx,j+dy
        if 0<=ni<3 and 0<=nj<3:
            ns = [r[:] for r in s]
            ns[i][j],ns[ni][nj] = ns[ni][nj],ns[i][j]
            yield ns
def solve(start):
    pq = [(h(start),0,start)]
    seen = {tuple(map(tuple,start)): None}
    cost = {tuple(map(tuple,start)): 0}
    while pq:
        _, g, curr = heapq.heappop(pq)
        if curr == goal: return curr
        for n in gen(curr):
            t = tuple(map(tuple,n))
            if t not in cost or g+1 < cost[t]:
                cost[t] = g+1
                seen[t] = curr
                heapq.heappush(pq, (g+1+h(n), g+1, n))
start = [list(map(int, input().split())) for _ in range(3)]
end = solve(start)
for row in end:
    print(' '.join(str(x) if x else '_' for x in row))
