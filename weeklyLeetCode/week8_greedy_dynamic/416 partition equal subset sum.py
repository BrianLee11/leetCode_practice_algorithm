# 416. Partition Equal Subset Sum
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Calculate the total sum of the array
        total_sum = sum(nums)
        
        # If the total sum is odd, we cannot partition it into equal subsets
        if total_sum % 2 != 0:
            return False
        
        # The target sum for each subset
        target = total_sum // 2
        
        # Use a dynamic programming approach to solve the problem
        # dp[i] represents whether a sum of 'i' can be achieved with the given numbers
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: sum of 0 is always possible
        
        # Iterate over each number in the input list
        for num in nums:
            # Iterate backward to avoid overwriting dp values in the current iteration
            for i in range(target, num - 1, -1):
                # Update dp[i] to be True if dp[i - num] was previously True
                dp[i] = dp[i] or dp[i - num]
        
        # The result is whether the target sum can be achieved
        return dp[target]
