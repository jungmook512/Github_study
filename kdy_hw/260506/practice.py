from graph2 import my_graph

def my_dfs(graph, start_node):
    stack = list()
    visited = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visited:
            stack.extend(reversed(graph[node]))
            visited.append(node)
    return visited

def my_bfs(graph, start_node):
    queue = list()
    visited = list()

    queue.append(start_node)

    while queue:
        node = queue.pop(0)

        if node not in visited:
            queue.extend(graph[node])
            visited.append(node)
    return visited

print(my_dfs(my_graph, 1))
print(my_bfs(my_graph, 1))

print("------------------------------")

maze = [
    [0, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 0]
]

def solve_maze(maze, start):
    stack = []
    visited = list()
    stack.append(start)

    while stack:
        r, c = stack.pop()      # pop된 튜플 데이터의 언패킹 과정
        if (r,c) not in visited:
            visited.append((r,c))

            # dr = -1, dc = 0
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                 nr, nc = r + dr, c + dc
                 
                 if 0 <= nc < 6 and 0 <= nr < 6:
                     pass

                 if 0<= nc < 6 and 0<= nr < 6 and maze[nr][nc] == 0:
                    stack.append((nr,nc))
    return visited

print(f"로봇 탐색 경로: {solve_maze(maze, (0,0))}")
    

