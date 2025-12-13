'''
387. First Unique Character in a String
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
'''

def firstUniqChar(s):
    char_count = {}
    
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    return -1

print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("aabb"))