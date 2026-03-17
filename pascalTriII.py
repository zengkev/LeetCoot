class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        # Start with the first element, which is always 1
        row = [1]
        for i in range(rowIndex):
            # Calculate the next element based on the current one
            # Next = Current * (rowIndex - i) / (i + 1)
            next_val = row[-1] * (rowIndex - i) // (i + 1)
            row.append(next_val)
        return row