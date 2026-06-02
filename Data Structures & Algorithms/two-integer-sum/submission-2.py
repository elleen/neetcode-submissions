class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, e in enumerate(nums):
            if target - e in set(nums[i+1:]):
                return [i, nums[i+1:].index(target-e)+i+1]