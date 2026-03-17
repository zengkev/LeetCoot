class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        output = []
        for i in range(numRows):
            # create a triangle of [1]s
            row = [1] * (i + 1)
            # we fill in the triangle
            for j in range(1, i):
                left = output[i-1][j-1]
                right = output[i-1][j]
                row[j] = left + right
            
            output.append(row)
        return output
