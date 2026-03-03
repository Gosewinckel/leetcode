class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        x = m - 1
        y = n - 1
        paths = [[-1] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                idx1 = x - i
                idx2 = y - j
                if idx1 == x or idx2 == y:
                    print(idx1)
                    paths[idx1][idx2] = 1
                    continue
                paths[idx1][idx2] = paths[idx1][idx2 + 1] + paths[idx1 + 1][idx2]
        return paths[0][0]


if __name__ == "__main__":
    m = 23
    n = 12
    sol = Solution()
    res = sol.uniquePaths(m, n)
    print(res)
