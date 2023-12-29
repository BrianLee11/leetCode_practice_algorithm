# intuition: Iterate each index until the target is reached

""" Approach: hash map table. 
Since there is only one unique solution, use hashmap. 

# In Python, the data structure dictionary. 
# Assigns the value of nums to its index
# example: nums[3,4,1] has hashmap{[3,0], [4,1], [1,2]}

# compute the complementary number that 
# target == complement + nums[index]

# search for complementary number in hashmap
# if found complement return its index
""" 

# Complexity
# Time complexity:
# O(n) since there are O(n) for loops

# Space complexity:
# $$O(n)$$ since hashmap stores n-number of elements from the num O(n)

class Solution:
    def twoSum(self, nums, target):
        # Use hashmap. In Python, the data structure dictionary
        hashmap = {}
        
        # assigns the value of nums to its index
        # example: nums[3,4,1] has hashmap{[3,0], [4,1], [1,2]}
        for index in range(len(nums)):
            hashmap[nums[index]] = index 
            
        for index in range(len(nums)):
            # compute the complementary number that 
            # target == complement + nums[index]
            complement = target - nums[index]
            
            # search for complementary number in hashmap
            # if found complement return its index
            if complement in hashmap and hashmap[complement] != index:
                return index, hashmap[complement]
            
# example
example = Solution()

# compute 
print(example.twoSum([3,2,4], 6)) # output: (1,2)






