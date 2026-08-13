class Solution:

    def containsDuplicates(self, section: List) -> bool:
        seen = set()
        for e in section:
            if e != "." and e in seen:
                return True
            seen.add(e)
        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [[None] * 9 for _ in range(9)]
        print(cols)
        sects = [[] for _ in range(9)]
        
        for i, row in enumerate(board):
            if self.containsDuplicates(row): return False
            
            for j, ele in enumerate(row):
                cols[j][i] = ele

                sec = (i // 3) + ((j//3)*3)
                print("putting ({}, {}) = {} in sec {}".format(i, j, ele, sec))
                sects[sec].append(ele)
         
        # print("sects", sects)

        for c in cols:
            if self.containsDuplicates(c): return False
        for s in sects:
            if self.containsDuplicates(s): return False
        return True
