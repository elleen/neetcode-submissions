import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_list = []
        for i, e in enumerate(nums):
            prod = math.prod(nums[0:i]) * math.prod(nums[i+1:])
            prod_list.append(prod)

        return prod_list