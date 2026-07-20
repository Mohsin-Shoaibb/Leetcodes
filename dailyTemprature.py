class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)

        stack = []

        answer = [0] * n

        for current in range(n):

            while stack and temperatures[current] > temperatures[stack[-1]]:

                previous = stack.pop()

                answer[previous] = current - previous
            
            stack.append(current)

        return answer
