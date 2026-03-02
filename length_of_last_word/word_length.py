class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        idx = len(s) - 1
        word = False
        while s[idx] != ' ' or not word:
            if idx < 0:
                break
            if s[idx] != ' ':
                word = True
            if word:
                length += 1
            idx -= 1
        return length
