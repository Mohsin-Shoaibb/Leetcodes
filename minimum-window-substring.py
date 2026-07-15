class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        
        required_dict = {}
        for char in t:
            required_dict[char] = required_dict.get(char,0) + 1

        current_dict = {}

        required = len(required_dict)
        formed = 0

        ans = (float('inf'),None,None)

        left, right = 0, 0

        while right < len(s):
            char = s[right]

            current_dict[char] = current_dict.get(char,0) + 1

            if char in required_dict and current_dict[char] == required_dict[char]:
                formed += 1
            
            while left <= right and formed == required:

                if (right - left + 1) < ans[0]:
                    ans = (right - left + 1, left, right)
                
                left_char = s[left]

                current_dict[left_char] -= 1

                if left_char in required_dict and current_dict[left_char] < required_dict[left_char]:
                    formed -= 1

                left += 1
            right += 1

        if ans[0] == float('inf'):
            return ""
        else:
            return s[ans[1]:ans[2] + 1]
