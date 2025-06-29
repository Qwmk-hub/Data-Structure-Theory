import sys
import re
class inventory:
    class _Node:
        __slots__ = '_element', '_next'
        def __init__(self, element, next_node=None):
            self._element = element
            self._next = next_node
    def __init__(self):
        self._head = self._tail = None
        self._size = 0
    def is_empty(self):
        return self._size == 0
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._head._element
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        result = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return result
    def enqueue(self, element):
        new_node = self._Node(element)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1

def quick_sort(S):
    if S._size < 2:
        return
    pivot = S.first()
    L = inventory()
    E = inventory()
    G = inventory()
    while not S.is_empty():
        x = S.first()
        if x[0] < pivot[0]:
            L.enqueue(S.dequeue())
        elif x[0] > pivot[0]:
            G.enqueue(S.dequeue())
        else:
            E.enqueue(S.dequeue())
    quick_sort(L)
    quick_sort(G)
    for Q in (L, E, G):
        while not Q.is_empty():
            S.enqueue(Q.dequeue())

def sort_inventory(avail, grid):
    limit = {item_id: max_qty for item_id, max_qty in avail}
    count = {}
    for row in grid:
        for cell in row:
            if cell == '-':
                continue
            item_id, quantity = cell
            count[item_id] = count.get(item_id, 0) + quantity
    flattened = []
    for item_id in sorted(count):
        total = count[item_id]
        max_unit = limit[item_id]
        while total > 0:
            use = min(total, max_unit)
            flattened.append((item_id, use))
            total -= use
    return flattened

if __name__ == "__main__":
    lines = sys.stdin.read().strip().split('\n')

    avail = [tuple(map(int, match)) for match in re.findall(r'\((\d+),(\d+)\)', lines[0])]

    grid = []
    for line in lines[1:]:
        row = []
        for match in re.finditer(r'\((\d+),(\d+)\)|-', line):
            if match.group(0) == '-':
                row.append('-')
            else:
                row.append((int(match.group(1)), int(match.group(2))))
        grid.append(row)

    result = sort_inventory(avail, grid)
    height, width = len(grid), len(grid[0]) if grid else 0
    output = [['-' for _ in range(width)] for _ in range(height)]

    k = 0
    for i in range(height):
        for j in range(width):
            if k < len(result):
                output[i][j] = result[k]
                k += 1

    for row in output:
        print(','.join(f'({item[0]},{item[1]})' if item != '-' else '-' for item in row))
