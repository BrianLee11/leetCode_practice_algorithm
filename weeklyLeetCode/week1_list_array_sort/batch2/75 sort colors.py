# 75. Sort Colors
# https://leetcode.com/problems/sort-colors/

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        1. Intuition: 
        - Sort all 2's and move all the 2's to the right-most. The result is a mix of (unsorted) 0's and 1's on the left part; all the 2's are located on the right part.
        - Sort all 1's and move all the 1's to the right of the 0's and the left of the 2's. 
        - Return the nums

        2. Approach: 
        - Use the while loop for each iteration. 
        - The first iteration moves all the 2's to the rightmost. Use swap. 
        - The second iteration moves all the 1's to the right of the 0's and the left of the 2's. Use swap. 

        3. Complexity:
        - Time complexity: O(n)
        - Space complexity: O(1)
        """
        length = len(nums)          # Time complexity: O(1), space complexity: O(1)
        left_index = 0              # Time comlexity: O(1), space complexity: O(1)
        right_index = length - 1    # Time complexity: O(1), space complexity: O(1)
        
        iteration_finished = False  # Time complexity: O(1), space complexity: O(1)
        
        # First iteration: move the 2's to the right
        # Each index is visited with the maximum number of visits of n-1
        # The total time complexity of this while loop: O(n), as inside the loop the maximum time complexity is O(1)
        # The total space complexity of this while loop: O(1), as inside the loop the maximum space complexity is O(1)
        while left_index < right_index and iteration_finished == False:  # Time complexity: O(1), space complexity: O(1)

            # Find the index on the left - should have a number 2.             
            # The while loop stops when nums[index] == 2 or index is out of bounds
            while left_index < length - 1 and nums[left_index] != 2:     # Time complexity: O(1), space complexity: O(1)
                left_index += 1                                          # Time complexity: O(1), space complexity: O(1)
            
            # Find the index on the right - should have a number other than 2 (i.e. 0 or 1)
            # The while loop stops when nums[index] == 0 or 1, or index is out of bounds
            while right_index > - 1 and nums[right_index] == 2:          # Time complexity: O(1), space complexity: O(1)
                right_index -= 1                                         # Time complexity: O(1), space complexity: O(1)
            
            # normal case for swap
            if left_index < right_index:
                nums[left_index], nums[right_index] = nums[right_index], nums[left_index]   # Time complexity: O(1), space complexity: O(1)
            
            else:
                iteration_finished = True        # Time complexity: O(1), space complexity: O(1)
        
        # Second iteration: move the 1's to the right of the 0's and left of the 2's. 
        # The total time complexity of this while loop: O(n), as inside the loop the maximum time complexity is O(1)
        # The total space complexity of this while loop: O(1), as inside the loop the maximum space complexity is O(1)
        iteration_finished = False
        left_index = 0
        while left_index < right_index and iteration_finished == False:
            while left_index < length - 1 and nums[left_index] != 1:
                left_index += 1
                
            while right_index > - 1 and nums[right_index] == 1:
                right_index -= 1
                
            if left_index < right_index:
                nums[left_index], nums[right_index] = nums[right_index], nums[left_index]
            
            else:
                iteration_finished = True        
        
    
        return nums # time complexity: O(1), space complexity: O(1)
