package q1_twoSum;

public class LeetCode9PalindromeNumbersNoString {
	public boolean isPalindrome(int x) {
		
		// Trivial case 1: Negative numbers are not palindromes
	    if (x < 0) {
	        return false;
	    }
	    
	    // Trivial case 2: single numbers are palindromes
	    if (x / 10 == 0) return true;
		
		// Non-trivial case
		// initialize variables
		int number1 = x; // for save
		int divisor = 1;
		
		// compute the divisor with given x
		while (x / 10 != 0) { // Check until all digits are processed			
			divisor *= 10;
			x = x / 10;
		}
				
		// checking for palindrome
		while (number1 / divisor != 0) {
			
			int last_digit = number1 % 10; 
			int first_digit = number1 / divisor;
			
			if (last_digit != first_digit) {
				return false; // Not a palindrome
			}
			else {
				number1 = (number1 % divisor) / 10; // Remove the first and last digit
				divisor /= 100; // Adjust the divisor
			}
			
		}
		return true; // Number is a palindrome
		
	}
	
	// main method inside the class
    public static void main(String[] args) {
    	LeetCode9PalindromeNumbersNoString solver = new LeetCode9PalindromeNumbersNoString();
        int nums = 10;
        boolean result = solver.isPalindrome(nums);
        System.out.println(result); // should be false, but output is true
    }
}
