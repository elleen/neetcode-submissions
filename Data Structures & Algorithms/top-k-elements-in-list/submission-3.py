import heapq

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = dict()
        for n in nums:
            if n not in nums_count.keys():
                nums_count[n] = 0
            nums_count[n] += 1
        
        min_heap = list()
        for key,val in nums_count.items():
            heapq.heappush(min_heap, (val,key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
                    
        return [y for x, y in min_heap]