class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        opening_braces = {'(':0,'{':1,'[':2}
        closing_braces = {')':0,'}':1,']':2}

        for char in s:
            
            if char in opening_braces:
                stack.append(char)

            elif char in closing_braces:
                if not stack:
                    return False
                
                check = stack.pop()

                if closing_braces[char] != opening_braces[check]:
                    return False

        if stack:
            return False
        return True
