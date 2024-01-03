package q1_twoSum;

import java.util.HashMap;

public class LeetCode1twoSumJavaHashMap {
	
    public int[] twoSum(int[] nums, int target) {
    	
        // Create a HashMap
        HashMap<Integer, Integer> hashmap = new HashMap<>();
    	
        // Assigns nums[i] to i
        // Example: nums = [2,4,6]. (2,0), (4,1), (6,2)
        for (int i = 0; i < nums.length; i++) {
        	hashmap.put(nums[i], i);
        }
        
        // Calculate the complement of the current element
        for (int i = 0; i < nums.length; i++) {
        	
            // Calculate the complement of the current element
        	int complement = target - nums[i]; // Corrected from target - i to target - nums[i]
        	
            // Check if the complement exists in the map and is not the current element
            if (hashmap.containsKey(complement) && hashmap.get(complement) != i) {
            	
                // If it exists, return the current index and the index of the complement
                return new int[] {i, hashmap.get(complement)};
            }
        }
        
        // If no solution is found, throw an exception or return null
        throw new IllegalArgumentException("No two sum solution");
    }

    // main method inside the class
    public static void main(String[] args) {
    	LeetCode1twoSumJavaHashMap solver = new LeetCode1twoSumJavaHashMap();
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] result = solver.twoSum(nums, target);
        System.out.println("Index 1: " + result[0] + ", Index 2: " + result[1]);
    }
}

