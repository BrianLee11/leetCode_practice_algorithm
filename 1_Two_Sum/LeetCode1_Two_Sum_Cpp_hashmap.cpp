/* Creation date: December 29, 2023
* gitHub URL: https://github.com/userNameWhere/leetCode_practice_algorithm
* an algorithm question from leetcode.com
Question: 1.two sum
File name: 1_Two_Sum_Cpp_hashmap.cpp
Intuition: iterate each index until target is reached
Approach: hashmap
Time complexity: O(n)
Space complexity: O(n)
*/

#include <iostream>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Create an unordered_map where both keys and values are integers
        unordered_map<int, int> hashmap;

        // Insert elements into hashmap
        for (int i = 0; i < nums.size(); i++) {
            hashmap[nums[i]] = i;
        }

        // Check if the complement exists in the hashmap
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];

            // Check if the complement exists in the map and is not the same element
            // This is O(1)
            if (hashmap.find(complement) != hashmap.end() && hashmap[complement] != i) {

                // If it exists, return the current index and the index of the complement
                return {i, hashmap[complement]};
            }
        }

        // If no solution is found, return an empty vector (or you might throw an exception)
        return {};

    }
};

int main() {
    
    // initialize
    Solution solution;

    // example 1
    vector<int> nums = {3,2,4};
    int target = 7;

    vector<int> result = solution.twoSum(nums, target); 

    cout << result[0] << ", " << result[1]; // output: 0,2

    return 0;
}
