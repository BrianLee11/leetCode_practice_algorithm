package q1_twoSum;

public class LeetCode1twoSumJavaBruteForce {

	public int[] twoSum(int[] nums, int target) {
	    
	    // This line will cause a compilation error because the size of the array is not specified.
	    // int[] result;
	    
	    for (int i = 0; i < nums.length; i++) {
	        for (int j = i + 1; j < nums.length; j++) { // Start j from i+1 to avoid using the same element twice
	            if (target == nums[i] + nums[j]) {
	                return new int[] {i, j}; // Return an array with the indices i and j
	            }
	        }
	    }
	    
	    // Return null or throw an exception if no solution is found.
	    // It's important to handle this case to avoid returning an uninitialized variable.
	    return null; // or throw an exception
	}

	
    // main method inside the class
    public static void main(String[] args) {
    	LeetCode1twoSumJavaBruteForce solver = new LeetCode1twoSumJavaBruteForce();
    	int[] nums = {2,5,7,9};
    	int target = 11;
    	int[] result = solver.twoSum(nums, target);
        //System.out.println(result[0] + " " + result[1]);
    }
}
