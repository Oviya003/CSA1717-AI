from collections import deque
def water_jug(a_cap, b_cap, target):
    visited = set()
    queue = deque()
    queue.append((0, 0))  
    while queue:
        a, b = queue.popleft()
        if (a, b) in visited:
            continue
        visited.add((a, b))
        print(f"A: {a}L, B: {b}L")
        if a == target or b == target:
            print("Target reached!")
            return
        states = [
            (a_cap, b),    
            (a, b_cap),     
            (0, b),         
            (a, 0),         
            (a - min(a, b_cap - b), b + min(a, b_cap - b)),  
            (a + min(b, a_cap - a), b - min(b, a_cap - a))   
        ]
        for state in states:
            if state not in visited:
                queue.append(state)

water_jug(4, 3, 2)
