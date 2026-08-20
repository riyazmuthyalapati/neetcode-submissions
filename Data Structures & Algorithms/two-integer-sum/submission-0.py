class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,j in enumerate(nums):
            result = target-j
            if result in seen:
                return [seen[result],i]
            seen[j]=i
        