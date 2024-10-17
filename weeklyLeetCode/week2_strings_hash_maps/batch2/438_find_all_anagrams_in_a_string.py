class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # Initialize arrays to store character counts
        p_count = [0] * 26
        s_count = [0] * 26
        result = []
        
        # Lengths of strings
        p_length = len(p)
        s_length = len(s)
        
        # Edge case: if pattern length is greater than string length, return empty list
        if p_length > s_length:
            return result
        
        # Initialize the character counts for the pattern and the first window of s
        for i in range(p_length):
            p_count[ord(p[i]) - ord('a')] += 1
            s_count[ord(s[i]) - ord('a')] += 1
        
        # Compare initial window
        if p_count == s_count:
            result.append(0)
        
        # Slide the window across the string `s`
        for i in range(p_length, s_length):
            # Add the next character to the current window
            s_count[ord(s[i]) - ord('a')] += 1
            # Remove the character that is left out of the window
            s_count[ord(s[i - p_length]) - ord('a')] -= 1
            
            # Compare current window with the pattern
            if s_count == p_count:
                result.append(i - p_length + 1)
        
        return result
