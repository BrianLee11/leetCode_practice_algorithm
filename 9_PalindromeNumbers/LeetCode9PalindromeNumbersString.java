package q1_twoSum;

public class LeetCode9PalindromeNumbersString {
	
	public boolean isPalindrome(int x) {
		
		// Convert the integer to a string
		String string1 = Integer.toString(x);
		
		// iterate
		int n = string1.length();
		for (int i = 0; i < n/2; i++) {
			
			if (string1.charAt(i) != string1.charAt(n-i-1)) {
				return false;
			}			
		}		
		
		return true;
	}
	
	// main method inside the class
    public static void main(String[] args) {
    	LeetCode9PalindromeNumbersString solver = new LeetCode9PalindromeNumbersString();
        int nums = 34543;
        boolean result = solver.isPalindrome(nums);
        System.out.println(result);
    }
}
