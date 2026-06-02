class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        for i, e in enumerate(nums):
            for j, f in enumerate(output):
                if i == j:
                    continue
                output[j] *= e
        
        return output