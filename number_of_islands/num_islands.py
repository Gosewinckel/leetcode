class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if f"[{i}, {j}]" not in visited and grid[i][j] == "1":
                    numIslands += 1
                    visited = self.exploreIslands(i, j, visited, grid)
        return numIslands

    def exploreIslands(self, i: int, j: int, visited: set(), grid: List[List[str]]) -> set():
        if f"[{i}, {j}]" not in visited and grid[i][j] == '1':
            visited.add(f"[{i}, {j}]")
            map = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for dir in map:
                x = i + dir[0]
                y = j + dir[1]
                if 0 <= x < len(grid) and 0 <= y < len(grid[x]):
                    visited = self.exploreIslands(x, y, visited, grid)
        return visited

if __name__ == "__main__":
    grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    sol = Solution()
    result = sol.numIslands(grid)
    print(result)
   
