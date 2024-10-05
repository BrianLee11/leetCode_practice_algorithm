# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]


        1. Intuition: 
        - Separate the product of pre-indexed numbers and the product of post-indexed numbers. 
        - Then multiply each product of pre-indexed and post-indexed numbers and set it equal to the product array's index. 

        2. Approach: 
        - Calculate the product of pre-indexed numbers and save in the prefix_product array. 
        - Calculate the product of post-indexed numbers and save in the post_product array. 
        - Calculate the product of prefix_product[index] and post_product[index] for each index in the product array. 
        - Return the product array. 

        3. Complexity:
        - Time complexity: O(n) due to three loops pass over the input array.
        - Space complexity: O(n) due to the use of prefix_product, post_product, and product_array.
        """

        length = len(nums)  #Time complexity: O(1), space complexity: O(1)

        product_array = [0] * length       # Time complexity: O(1), space compleixty: O(n)
        prefix_product = [1] * length      # Time complexity: O(1), space complexity: O(n)
        post_product = [1] * length        # Time compleixty: O(1), space complexity: O(n)

        # The total time complexity of this for loop: O(n)
        # The total space comlexity of this for loop: O(1)
        # Index is visited by the number of length, visited only once. 
        for index in range(1, length):
            prefix_product[index] = prefix_product[index - 1] * nums[index - 1] # Time complexity: O(1), space complexity: O(1)
            # In an array, search the value of a given index has the time complexity of O(1)
            # Space complexity is O(1), as using only a fixed few number of variables.

        # The total time complexity of this for loop: O(n)
        # The total space comlexity of this for loop: O(1)
        # The same logic applies to the previous for loop. 
        for index in range(length - 2, -1, -1):
            post_product[index] = post_product[index + 1] * nums[index + 1]
   
        # The total time complexity of this for loop: O(n)
        # The total space comlexity of this for loop: O(1)
        # The same logic applies to the previous for loop.
        for index in range(length):
            product_array[index] = prefix_product[index] * post_product[index]

        return product_array  # The total time complexity is O(1), the total space complexity is O(1)
        
