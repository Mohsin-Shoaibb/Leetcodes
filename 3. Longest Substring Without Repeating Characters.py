class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_window = 0
        seen = {}
        
        for right, char in enumerate(s):

            if char in seen and seen[char] >= left:
                left = seen[char] + 1

            seen[char] = right

            max_window = max(max_window,right - left + 1)
        
        return max_window
