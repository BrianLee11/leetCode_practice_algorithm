/* Creation date: August 9, 2023
* Modified date: December 23, 2023
* gitHub URL: https://github.com/userNameWhere/leetCode_practice_algorithm
* an algorithm question from leetcode.com
Question: 1.two sum
File name: 1_Two_Sum_Cpp_brute_force.cpp 
Intuition: iterate each index until target is reached
Approach: brute force 
Time complexity: O(n^2)
Space complexity: O(1)
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector <int> twoSum(vector<int> nums, int target) {

        // constructor
        // declare a vector to store the result indices
        vector <int> result;

        // iterate through the vector using nested loops
        for (int i = 0; i < nums.size(); i++) {

            for (int j = i + 1; j < nums.size(); j++) {

                if (target == nums[i] + nums[j]){
                    // add the indices i and j to result
                    result.push_back(i);
                    result.push_back(j);

                    return result;
                }
            }
        }

        // If no such pair is found, an empty result vector is returned
        return result;
    }
};

// declare a function. Define after int main()
void printVector(vector <int> result);

int main() {

    // initialize
    Solution solution;

    // example 1
    vector<int> nums = {3,2,4};
    int target = 6; 

    vector<int> result = solution.twoSum(nums, target);
    printVector(result); // input is [1,2]
}

// define function
void printVector(vector <int> result) {

    // display elements
    cout << "Output: [";
    for (int i = 0; i < result.size() - 1; i++) {

        if (i != result.size() - 1) {
            cout << result[i] << ", ";
        }
        else {
            cout << result[i];
        }
    }
    cout << "]" << endl;
}
