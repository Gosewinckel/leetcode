class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        # binary search
        while left <= right:
            mid = left + (right - left)//2
            # found case
            if target == nums[mid]:
                return mid
            # normal case binary search
            if nums[left] <= nums[right]:
                if target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid -1

            # split binary search
            else:
                # move right
                if (nums[mid] < target and target <= nums[right]):
                    left = mid + 1
                    continue

                # move left
                elif (nums[mid] > target and target > nums[right]):
                    right = mid - 1
                    continue

                #dynamic cases
                elif nums[mid] < target:
                    if nums[mid] <= nums[right]:
                        right = mid - 1
                    elif nums[mid] > nums[right]:
                        left = mid + 1
                elif nums[mid] > target:
                    if nums[mid] > nums[right]:
                        left = mid + 1
                    elif nums[mid] <= nums[right]:
                        right = mid - 1


        return -1

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    sol = Solution()
    res = sol.search(nums, target)
    print(res)
