class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_max = 0
        for i in nums:
            if current_max < 0:
                current_max = 0
            current_max+=i
            max_sum = max( current_max, max_sum)
        return max_sum
                
        