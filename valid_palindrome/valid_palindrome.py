class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        s = s.lower()
        ptr1 = 0
        ptr2 = len(s) - 1
        while True:
            if s[ptr1].isalnum() and s[ptr2].isalnum():
                if s[ptr1] != s[ptr2]:
                    return False
                else:
                    ptr1 += 1
                    ptr2 -= 1
            elif not s[ptr1].isalnum():
                ptr1 +=1
            elif not s[ptr2].isalnum():
                ptr2 -= 1

            if ptr1 > ptr2:
                break

        return True


if __name__ == "__main__":
    s = "v' 5:UxU:5v'"
    solution = Solution()
    result = solution.isPalindrome(s)
    print(result)

