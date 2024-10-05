# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        1. Intuition: For each number in the array, we can calculate its complement (= target - number). 
        If the complement exists in the array (specifically, among the numbers we have already processed), then we have found the two numbers. 
        The solution leverages a dictionary (hash table) to store the numbers and their indices we have processed. This allows quick check if the complement exists. 
        
        2. Approach: use dictionary (hash table), calculate a number's complement, look through dictionary to find index. 
        
        3. Complexity:
        - Time complexity: O(n) as we visit each element once. We traverse the array once, and dictionary operations (insertions and lookups) take constant time on average.
        - Space complexity: O(n) as we store each element in the dictionary.  In the worst case, we may store all n elements of the array in the dictionary if no solution is found early.
        """

        # initialize a dictionary 
        # Time complexity: O(1)
        # Space complexity: O(1)
        dictionary = {}

        # Loop through the numbers array
        # visit number in the array numbers once
        # The total time complexity of the for loop is O(n) because inside the for loop, the time complexity is O(1)
        # The total space complexity of the for loop is O(n) because inside the for loop, the space complexity is O(1)
        
        for index in range(len(numbers)):
            reciprocal = target - numbers[index]                 # time complexity: O(1), space complexity: O(1)

            # Check if the reciprocal exists in the dictionary
            if reciprocal in dictionary:                         # time compleixty: O(1) as searching in hash table. Space complexity: O(1)
                return [dictionary[reciprocal] + 1, index + 1]   # time complexity: O(1) as simple operation. Space compleixty: O(1)
            else:
                 # Store the current number with its index
                dictionary[numbers[index]] = index               # time complexity: O(1) as adding a (key,value)in hash table is constant operation. Space complexity: O(1)
