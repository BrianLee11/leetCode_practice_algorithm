# intuition: Iterate each index until the target is reached

# Approach: Brute force using the for loops. 
# Once the target is reached, return two indices and exit.

# Complexity
# Time complexity:
# O(n^2) since there are two for loops. 

# Space complexity:
# $$O(1)$$ since nums[index1] and nums[index2] are O(1) 
# and so is target = nums[index1] + nums[index2]

# Brute-force method
class Solution:
    def twoSum(self, nums, target):
        for index1 in range(len(nums)):
           for index2 in range(index1+1, len(nums)):
               if target == nums[index1] + nums[index2]:
                   return index1, index2

# example: initialize example1 
example1 = Solution()

# print the indices of nums so that nums[index1] + nums[index2] = target
print(example1.twoSum([3,2,4],6)) # output: (1, 2)


