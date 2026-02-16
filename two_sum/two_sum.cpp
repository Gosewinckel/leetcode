#include <iostream>
#include <unordered_map>
#include <vector>

class Solution {
	public:
		std::vector<int> twoSum(std::vector<int>& nums, int target) {
			std::unordered_map<int, int> indexMap;
			std::vector<int> output;
			for(int i = 0; i < nums.size(); ++i) {
				int comp = target - nums[i];
				// if found
				if(indexMap.count(comp) != 0) {
					output.push_back(indexMap[comp]);
					output.push_back(i);
					return output;
				}
				//if not found
				else {
					indexMap[nums[i]] = i;
				}
			}
			return output;
		}
};

int main() {
	std::vector<int> nums = {1, 2, 3};
	int target = 5;
	
	Solution solution;
	std::vector<int> result = solution.twoSum(nums, target);

	std::cout << "results: " << result[0] << result[1];
}
