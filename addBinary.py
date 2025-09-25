'''
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        '''
        1 + 1 = 10
        1 + 0 = 1
        0 + 1 = 1
        0 + 0 = 0
        
        '''
        result = ""
        carry = 0 

        # pointers fro the end of the strings
        i, j = len(a) - 1, len(b) - 1

        # loop until both strings are processed and no carry is left
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            if i >= 0:
                total += int(a[i])
                i -= 1
            
            if j >= 0:
                total += int(b[j])
                j -= 1
            
            # calculate the new digit and the new carry
            result = str(total % 2) + result
            carry = total // 2

        return result
    
    def addBinary2(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)

        
        return bin(a+b)[2:]