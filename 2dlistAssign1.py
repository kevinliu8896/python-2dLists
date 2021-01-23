# Kevin Liu
# 105191861

def empty(g):
    for row in range(len(g)):
        for col in range(len(g[row])):
            if g[row][col] != 0:
                return False
    else:
        return True


def find(g, value):
    index0 = 0
    index1 = 0

    for row in range(len(g)):
        for col in range(len(g[row])):
            if g[row][col] == value:
                index0 = row
                index1 = col
                return [index0, index1]
    else:
        return [-1, -1]


grid = [
    [0, 34, 67],
    [44, 5, 3],
    [7, 8, 9]
]
print("empty(grid) -> ", empty(grid))
print("find(grid) -> ", find(grid, 67))

print("=========================================================================================================")
print()

grid2 = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
print("empty(grid) -> ", empty(grid2))
print("find(grid) -> ", find(grid2, 67))

