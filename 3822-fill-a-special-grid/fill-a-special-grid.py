class Solution(object):
    def specialGrid(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
class Solution(object):
    def specialGrid(self, n):
        grid = [[0]]

        for _ in range(n):
            size = len(grid)
            new = [[0] * (size * 2) for _ in range(size * 2)]
            
            for i in range(size):
                for j in range(size):
                    new[i][j + size] = grid[i][j]
                    new[i + size][j + size] = grid[i][j] + size * size
                    new[i + size][j] = grid[i][j] + 2 * size * size
                    new[i][j] = grid[i][j] + 3 * size * size
            
            grid = new

        return grid 