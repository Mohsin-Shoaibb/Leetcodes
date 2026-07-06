class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        ans = set()
        length = len(nums)

        for i in range(length):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = length - 1

            while j < k:

                sum = nums[i] + nums[j] + nums[k]

                if sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    ans.add((nums[i],nums[j],nums[k]))
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j-1]:
                        j += 1
        
        return [list(triplet) for triplet in ans]
