maze = [
    [0, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 0]
]

for i in maze:
    print(i)

print("------------------------------------")

# 세로(행), 가로(열) 입력
rows = int(input("세로(행) 크기 입력: "))
cols = int(input("가로(열) 크기 입력: "))

maze = []

print(f"\n{rows}행 {cols}열의 데이터를 입력하세요. (공백으로 구분)")

for i in range(rows):
    while True:
        data = list(map(int, input(f"{i+1}행 입력: ").split()))
        if len(data) == cols:
            maze.append(data)
            break
        else:
            print(f"⚠️ {cols}개의 값을 입력해야 합니다. 다시 입력하세요.")

print("\n생성된 미로:")
for row in maze:
    print(row)

print("------------------------------------")

from collections import deque

def solve_maze_bfs(maze, start):
    queue = deque()         # ← stack = [] 에서 변경
    visited = list()
    queue.append(start)

    while queue:
        r, c = queue.popleft()      # ← stack.pop() 에서 변경 (FIFO)

        if (r, c) not in visited:
            visited.append((r, c))

            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nc < 6 and 0 <= nr < 6:
                    pass

                if 0 <= nc < 6 and 0 <= nr < 6 and maze[nr][nc] == 0:
                    queue.append((nr, nc))  # ← stack.append 에서 변경

    return visited

print(f"로봇 탐색 경로: {solve_maze_bfs(maze, (0,0))}")