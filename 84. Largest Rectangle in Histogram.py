class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        left = []
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            left.append(stack[-1] if stack else -1)
            stack.append(i)

        right = []
        stack = []
        for i in reversed(range(n)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            right.append(stack[-1] if stack else n)
            stack.append(i)
            
        right.reverse() 

        ans = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            ans = max(ans, heights[i] * width)

        return ans
