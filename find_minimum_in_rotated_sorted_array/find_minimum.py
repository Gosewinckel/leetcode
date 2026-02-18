class Solution:
    def findMin(self, nums: List[int]) -> int:
        lowest = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            centre = left + (right - left) // 2
            if nums[centre] <= nums[len(nums) - 1]:
                lowest = nums[centre]
                right = centre - 1
            else:
                left = centre + 1
        return lowest


if __name__ == "__main__":
    nums = [1, 2, 3, -10]
    sol = Solution()
    ans = sol.findMin(nums)
    print(ans)
