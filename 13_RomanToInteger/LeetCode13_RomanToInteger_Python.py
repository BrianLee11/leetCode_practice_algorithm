"""
LeetCode 
Question: 13. Roman to Integer
Task: Given a roman numeral, convert it to an integer.

(symbol, value)
(I, 1)
(V, 5)
(X, 10)
(L, 50)
(C, 100)
(D, 500)

(IV, 4)
(IX, 9)

(XL, 40)
(XC, 90)

(CD, 400)
(CM, 900)

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # initialize variable
        number = 0
        i = 0
        
        while i < len(s):
            
            # case 1: I
            if s[i] == "I":
                if i+1 < len(s): # check validity of the next index
                    if s[i+1] == "V":
                        number += 4
                        i = i + 2 # jump index by 2, instead of 1
                        continue # move on the while loop, skip anything below
                    elif s[i+1] == "X":
                        number += 9
                        i = i + 2
                        continue
                    else:
                        number += 1
                else:
                    number += 1
            
            # case 2: X
            elif s[i] == "X":
                if i+1 < len(s):
                    if s[i+1] == "L":
                        number += 40
                        i = i + 2 
                        continue
                    elif s[i+1] == "C":
                        number += 90
                        i = i + 2 
                        continue
                    else:
                        number += 10
                else:
                    number += 10
                
            # case 3: C
            elif s[i] == "C":
                if i+1 < len(s):
                    if s[i+1] == "D":
                        number += 400
                        i = i + 2 
                        continue
                    elif s[i+1] == "M":
                        number += 900
                        i = i + 2 
                        continue
                    else:
                        number += 100
                else:
                    number += 100
                    
            # case 4: V
            elif s[i] == "V":
                number += 5
                
            # case 5: L
            elif s[i] == "L":
                number += 50
                
            # case 6: D
            elif s[i] == "D":
                number += 500
            
            # case 7: M
            elif s[i] == "M":
                number += 1000
        
            # Only increment if a two-character numeral wasn't found
            i += 1 
            
        return number

# test 
solution = Solution()

#print(solution.romanToInt("III"))      # output: 3
#print(solution.romanToInt("LVIII"))    # output: 58
#print(solution.romanToInt("MCMXCIV"))  # output: 1994
print(solution.romanToInt("MMMC"))  # output: 3100


        