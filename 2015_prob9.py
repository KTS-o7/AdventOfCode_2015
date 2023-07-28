"""class Solution(object):
    def minPathSum(self, grid):
        row = len(grid) - 1
        col = len(grid[0]) - 1
        print(row, col)
        i = row - 1
        j = col - 1
        while j >= 0:
            grid[row][j] += grid[row][j + 1]
            j -= 1
        while i >= 0:
            grid[i][col] += grid[i + 1][col]
            i -= 1
        j = col - 1
        i = row - 1
        while i >= 0:
            while j >= 0:
                grid[i][j] += min(grid[i][j + 1], grid[i + 1][j])
                j -= 1
            j = col - 1
            i -= 1
        return grid[0][0]


ob1 = Solution()
print(
    ob1.minPathSum(
        [
            [0, 66, 28, 60, 34, 34, 3, 108],
            [66, 0, 22, 12, 91, 121, 111, 71],
            [28, 22, 0, 39, 113, 130, 35, 40],
            [60, 12, 39, 0, 63, 21, 57, 83],
            [34, 91, 113, 63, 0, 9, 50, 60],
            [34, 121, 130, 21, 9, 0, 27, 81],
            [3, 111, 35, 57, 50, 27, 0, 90],
            [108, 71, 40, 83, 60, 81, 90, 0],
        ]
    )
)
"""

import sys
from itertools import permutations

places = set()
distances = dict()
for line in open("2015_prob9_input.txt"):
    (source, _, dest, _, distance) = line.split()
    places.add(source)
    places.add(dest)
    distances.setdefault(source, dict())[dest] = int(distance)
    distances.setdefault(dest, dict())[source] = int(distance)

shortest = sys.maxsize
longest = 0
for items in permutations(places):
    dist = sum(map(lambda x, y: distances[x][y], items[:-1], items[1:]))
    shortest = min(shortest, dist)
    longest = max(longest, dist)

print("shortest: %d" % (shortest))
print("longest: %d" % (longest))
