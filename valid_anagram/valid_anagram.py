class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        inWord = dict()
        for i in s:
            if i in inWord:
                inWord[i] += 1
            else:
                inWord[i] = 1
        for i in t:
            if i in inWord and inWord[i] > 0:
                inWord[i] -= 1
            else:
                return False
        return True

if __name__ == "__main__":
    s = "aaab"
    t = "aaaa"
    sol = Solution()
    res = sol.isAnagram(s, t)
    print(res)
