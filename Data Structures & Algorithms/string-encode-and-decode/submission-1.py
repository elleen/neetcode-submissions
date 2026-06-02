class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += "#{}@{}".format(len(s), s)

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = list()

        decode_len_start = None
        to_decode = None
        current_str = ""
        for i,c in enumerate(list(s)):
            if to_decode is not None and to_decode > 0:
                current_str += c
                to_decode -= 1

            elif c == '@':
                to_decode = int(s[decode_len_start:i])

            elif c == '#':
                decode_len_start = i+1

            if to_decode == 0:
                decoded.append(current_str)

                # Reset variables
                to_decode = None
                current_str = ""



        return decoded