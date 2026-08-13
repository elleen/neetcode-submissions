import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            2: ['a','b','c'],
            3: ['d','e','f'],
            4: ['g','h','i'],
            5: ['j','k','l'],
            6: ['m','n','o'],
            7: ['p','q','r','s'],
            8: ['t','u','v'],
            9: ['w','x','y','z']
        }
        if len(digits) == 0: return []
        list_of_chars = [phone[int(i)] for i in digits]
        return [''.join(x) for x in list(itertools.product(*list_of_chars))]