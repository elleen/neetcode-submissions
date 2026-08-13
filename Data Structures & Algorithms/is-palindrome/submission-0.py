import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        stack = list()
        halfway = len(st) // 2

        for char in st[:halfway]:
            stack.append(char)
        
        to_check = st[halfway:]
        if len(st) % 2 == 1: 
            to_check = st[halfway+1:]

        for c2 in to_check:
            if c2 != stack.pop():
                return False
        return True