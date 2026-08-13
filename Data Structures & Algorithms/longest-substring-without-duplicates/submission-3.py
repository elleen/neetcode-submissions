class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_substr = list()
        longest_len = 0
        for c in s:
            if c in current_substr:
                if len(current_substr) > longest_len:
                    longest_len = len(current_substr)
                
                while True:
                    popped_char = current_substr.pop(0)
                    if popped_char == c:
                        break
                
            current_substr.append(c)
        

        if len(current_substr) > longest_len:
            longest_len = len(current_substr)
        return longest_len