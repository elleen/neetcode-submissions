class Solution:
    def countLetters(self, string: str) -> dict:
        letter_count = dict()
        for c in string:
            if c not in letter_count.keys():
                letter_count[c] = 1
                continue
            letter_count[c] += 1
        return letter_count

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        s_letter_count = self.countLetters(s)
        t_letter_count = self.countLetters(t)

        return s_letter_count == t_letter_count
