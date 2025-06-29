import sys
from collections import deque

def main():
    lines = [line.strip() for line in sys.stdin]
    height = len(lines)
    width = len(lines[0]) if height > 0 else 0
    graph = {}
    start = end = None
    for y in range(height):
        for x in range(width):
            char = lines[y][x]
            if char in '0AB':
                node = f'({y},{x})'
                if char == 'A':
                    start = node
                if char == 'B':
                    end = node
                graph[node] = []

                for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < height and 0 <= nx < width:
                        neighbor_char = lines[ny][nx]
                        if neighbor_char in '0AB':
                            neighbor = f'({ny},{nx})'
                            graph[node].append(neighbor)
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    while queue:
        current = queue.popleft()
        if current == end:
            break
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
    path = []
    current = end
    while current:
        y, x = map(int, current[1:-1].split(','))
        path.append((y, x))
        current = parent[current]
    print(len(path) - 1)
if __name__ == "__main__":
    main()
