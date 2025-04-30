from collections import deque
def is_valid(m, c):
    return (m == 0 or m >= c) and (3 - m == 0 or 3 - m >= 3 - c)
def get_successors(m, c, boat):
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
    successors = []
    for dm, dc in moves:
        if boat == 1:
            nm, nc = m - dm, c - dc
        else:
            nm, nc = m + dm, c + dc
        if 0 <= nm <= 3 and 0 <= nc <= 3 and is_valid(nm, nc):
            successors.append((nm, nc, 1 - boat))
    return successors
def solve():
    start = (3, 3, 1)  
    goal = (0, 0, 0)
    visited = set()
    queue = deque([(start, [])])
    while queue:
        state, path = queue.popleft()
        if state in visited:
            continue
        visited.add(state)
        path = path + [state]
        if state == goal:
            for step in path:
                print(f"M:{step[0]} C:{step[1]} Boat:{'Left' if step[2] else 'Right'}")
            return
        for next_state in get_successors(*state):
            if next_state not in visited:
                queue.append((next_state, path))
solve()
