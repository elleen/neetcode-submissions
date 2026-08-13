class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target > row[-1]:
                continue
            if target < row[0]:
                return False
            
            for e in row:
                if e == target:
                    return True
            
        return False