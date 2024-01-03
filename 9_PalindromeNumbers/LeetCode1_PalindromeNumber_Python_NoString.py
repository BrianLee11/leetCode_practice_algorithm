"""
Creation date: January 2, 2024
LeetCode problem 
Topic: 9. Palindrome Number
Goal: Given an integer x, return true if x is a palindrome, 
and false otherwise. Solves the "follow up" part.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, 
it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up: Could you solve it without converting the integer to a string?
"""

"""
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Use quotient and remainders. 

# Approach
<!-- Describe your approach to solving the problem. -->
Negative numbers are false. Single nubmers are true.
Use the while loop statements to compare the first digit and last digit.
Then, update the divisor and number. 

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
O(n)

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
O(1)

"""
# Codes: 
class Solution(object):

    def isPalindrome(self, number1):
        """
        :type number1: int
        :rtype: bool
        """
        
        # Early checks for negative and single-digit numbers
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        if number1 < 0 or (number1 != 0 and number1 % 10 == 0):
            return False
        
        if number1 // 10 == 0:
            return True
        
        # Initialize variables
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        num = number1
        divisor = 10
        power = 0

        # Calculate the number of digits in the number
        # Time Complexity: O(log(10) n)
        # Space Complexity: O(1)
        while (number1 // divisor != 0):
            power += 1
            number1 = number1 // divisor

        divisor = pow(10, power)

        # Compare digits from the ends towards the middle
        # Time Complexity: O(n/2)
        # Space Complexity: O(1)
        while (num != 0):
            last_digit = num % 10
            first_digit = num // divisor
            
            if last_digit != first_digit:
                return False
            
            num = (num % divisor) // 10
            divisor = divisor // 100
            
        return True
        # Total Time Complexity: O(n)
        # Total Space Complexity: O(1)

    
# Test 
string1 = 121
string2 = -121
string3 = 10

solution = Solution()

print(solution.isPalindrome(string1)) #True
print(solution.isPalindrome(string2)) #False
print(solution.isPalindrome(string3)) #False

