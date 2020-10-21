class Solution:
    def spiralOrder(self, matrix):
        if matrix == []:
            return []
        startRow = startCol = 0
        endRow = len(matrix) - 1
        endCol = len(matrix[0])  - 1
        
        final_array = []
        
        while startRow <= endRow and startCol <= endCol:
            
            pointerA = startCol
            while pointerA <= endCol:
                final_array.append(matrix[startRow][pointerA])
                pointerA += 1
            startRow += 1
            
            pointerB = startRow
            while pointerB <= endRow:
                final_array.append(matrix[pointerB][endCol])
                pointerB += 1
            endCol -= 1
            
            pointerC = endCol
            if startRow <= endRow: # This condition is helpful for rectangular matrices
                while pointerC >= startCol:
                    final_array.append(matrix[endRow][pointerC])
                    pointerC -= 1
                endRow -= 1
            
            pointerD = endRow
            if startCol <= endCol: # This condition is helpful for rectangular matrices
                while pointerD >= startRow:
                    final_array.append(matrix[pointerD][startCol])
                    pointerD -= 1
                startCol += 1
            
        return final_array

if __name__ == "__main__":
    array = [[1,2,3],[4,5,6],[7,8,9]]
    soln = Solution()
    spiral_arr = soln.spiralOrder(array)
    print(spiral_arr)
