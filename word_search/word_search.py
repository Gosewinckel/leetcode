class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        coords = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        # loop through all board entries
        for i in range(len(board)):
            for j in range(len(board[0])):
                # if matches first letter, search for word
                if board[i][j] == word[0]:
                    result = self.search(board, i, j, word, 0, visited, coords)
                    if result:
                        return True
        return False

    def search(self, board: List[List[str]], i: int, j: int, word: str, idx: int, visited: List[List[bool]], coords: List[List[int]]) -> bool:
        # place has already been used in word
        if visited[i][j]:
            return False
        visited[i][j] = True

        # check if pos is the next letter
        if board[i][j] != word[idx]:
            visited[i][j] = False
            return False

        # found all letters inorder
        if idx == len(word) - 1 and board[i][j] == word[idx]:
            return True

        for dir in coords:
            if 0 <= i + dir[0] < len(board) and 0 <= j + dir[1] < len(board[0]):
                if self.search(board, i + dir[0], j + dir[1], word, idx + 1, visited, coords):
                    return True
        visited[i][j] = False
        return False

if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] 
    word = "ABCCED"
    sol = Solution()
    result = sol.exist(board, word)
    print(result)
