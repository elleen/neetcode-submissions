class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = dict()
        for s in strs:
            sorted_s = str(sorted(s))
            if sorted_s not in anagram_dict.keys():
                anagram_dict[sorted_s] = list([s])
                continue
            anagram_dict[sorted_s].append(s)
            
        return [v for _,v in anagram_dict.items()]