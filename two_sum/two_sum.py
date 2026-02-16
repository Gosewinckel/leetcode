
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        output = []
        for i in range(len(nums)):
            num = nums[i]
            dict[num] = i

            #check if other component is in dict
            comp = target - num
            if comp in dict.keys():
                output = [dict[comp], i]
                print("1")
                return output
    
        return output


if __name__ == "__main__":
    sol = Solution()
    list = [2, 3]
    target = 5
    nums =  sol.twoSum(list, target)
    print(nums)
