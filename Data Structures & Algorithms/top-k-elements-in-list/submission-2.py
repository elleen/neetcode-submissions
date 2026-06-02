class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = dict()

        for n in nums:
            if n not in nums_count.keys():
                nums_count[n] = 0
            nums_count[n] += 1

        top_freq = sorted(nums_count, key=nums_count.get, reverse=True)

        return top_freq[:k]
                    
        