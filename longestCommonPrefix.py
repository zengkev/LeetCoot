'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.

'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Take first letter of the string and compare with other
        # if no match output explanation
        # if match iterate onto second then break
        if not strs:
            print('NO Prefix matches')

        for i, char in enumerate(strs[0]):
            # check this character with other first char
            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]
        return strs[0]