# https://leetcode.com/problems/first-unique-character-in-a-string/
# Had to research as first implimentation used two passes and had a bad O notation
class Solution:
    def firstUniqChar(self, s: str) -> int:
        characters = 26
        visted = [-1] * characters
        
        for i in range(len(s)):
            # Index = current letter index - a
            index = ord(s[i]) - ord('a')

            # if initialised value; overwrite
            if visted[index] == -1:
                visted[index] = i
            # mark repeated values
            else:
                visted[index] = -2

        indx = -1
        # Iterate through visted characters
        for i in range(characters):
            if visted[i] >= 0 and (indx == -1 or visted[i] < visted[indx]):
                indx = i
        return -1 if indx == -1 else visted[indx]
