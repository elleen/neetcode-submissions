class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        starting_nums = list()
        num_set = set(nums)

        for n in nums:
            if n-1 not in num_set:
                starting_nums.append(n)
        
        longest = 0
        for sn in starting_nums:
            it = sn
            consec = 1
            while it+1 in num_set:
                consec += 1
                it += 1
            if consec > longest:
                longest = consec

        return longest