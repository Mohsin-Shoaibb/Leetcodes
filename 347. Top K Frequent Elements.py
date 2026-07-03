class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counted = {}

        for num in nums:
            counted[num] = 1 + counted.get(num,0)

        heap = []

        for key, value in counted.items():
            heapq.heappush(heap,(value,key))
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        for frequency, element in heap:
            result.append(element)
        
        return result
