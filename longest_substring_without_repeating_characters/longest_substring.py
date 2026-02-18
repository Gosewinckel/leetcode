class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        highest = 1
        ptr1 = 0
        ptr2 = 1
        characters = set()
        
        characters.add(s[ptr1])
        while ptr2 < len(s):
            while s[ptr2] in characters:
                characters.remove(s[ptr1])
                ptr1 += 1

            characters.add(s[ptr2])
            ptr2 += 1
            if ptr2 - ptr1 > highest:
                highest = ptr2 - ptr1

        return highest

if __name__ == "__main__":
    s = "shitfaced"
    sol = Solution()
    result = sol.lengthOfLongestSubstring(s)
    print(result)
