class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = {}
        longest = k
        most = 0
        idx1 = 0
        idx2 = 0
        #fill dict with starting letters
        for i in range(k):
            if s[i] in letters:
                letters[s[i]] += 1
            else:
                letters[s[i]] = 1
            if letters[s[i]] > most:
                most = letters[s[i]]
            idx2 += 1
        
        while idx2 < len(s):
            # expand window and add new letter to dict
            if s[idx2] in letters:
                letters[s[idx2]] += 1
                # if new letter is most numerous transform other letters
                if letters[s[idx2]] > most:
                    most = letters[s[idx2]]
            else:
                letters[s[idx2]] = 1
                if letters[s[idx2]] > most:
                    most = letters[s[idx2]]

            # if k to spare
            if k + most >= (idx2 - idx1) + 1:
                longest = idx2 - idx1 + 1
            # if window exceeds possible transforms + letter, move forward
            elif k + most < (idx2 - idx1) + 1:
                letters[s[idx1]] -= 1
                idx1 += 1
            idx2 += 1
            
        return longest

if __name__ == "__main__":
    s = "CABABBCCACAC"
    k = 1
    sol = Solution()
    res = sol.characterReplacement(s, k)
    print(res)
