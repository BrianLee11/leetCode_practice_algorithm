"""
Creation date: January 2, 2024
LeetCode problem 
Topic: 9. Palindrome Number
Goal: Given an integer x, return true if x is a palindrome, 
and false otherwise.

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
Change the input x's data type to string. 
Then, use for loop on string[0], string[1], ... and compare. 

# Approach
<!-- Describe your approach to solving the problem. -->
For any index, if string[index] != string[length of string - index - 1] then:
    return False (not palindrome)

Otherwise, continue. with i = i + 1

If index reaches the middle number, return True (palindrome)

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
O(n), since the indices are visited from 0 to middle number of the string, 
so O(n/2). But in Big O notation, we drop the constants and lower-order terms.
Hence O(n). 

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
O(1). Recall space complexity = fixed space + variable space.

Fixed space: x, string1, i in my codes: this space does not grow with 
the size of the input and is considered O(1) or constant space.
The variables x, i, and string1 use fixed space. 
Regardless of the size of x, the space needed for these variables doesn't grow.

Variable space: used by dynamic data structures 
(like lists, stacks, or strings that grow with input size). 
The space needed can change during the execution of the algorithm.
I convert the integer x into a string and store it in string1. 
While it might seem this is variable space, it's a bit nuanced. 
The size of string1 is proportional to the number of digits in x, 
which grows logarithmically with x. 
For instance, an integer x with a value of 1000 has 4 digits, 
so string1 will have a length of 4. 
Even if x grows to 10000, string1 will only have a length of 5.
Here, there is no dynamic data structure. 
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Early check for negative numbers
        if x < 0:
            return False
        
        # Convert the integer to a string for easy character comparison
        string1 = str(x)
        
        # Iterate through the string up to the middle character
        for i in range(int(len(string1)/2) + 1):
            # If mirrored characters don't match, it's not a palindrome
            if string1[i] != string1[len(string1)-i-1]:
                return False  # Mismatch found, no need to check further
                
        # If no mismatches found, it's a palindrome
        return True

# Test 
string1 = 121
string2 = -121
string3 = 10

solution = Solution()

print(solution.isPalindrome(string1)) #True
print(solution.isPalindrome(string2)) #False
print(solution.isPalindrome(string3)) #False