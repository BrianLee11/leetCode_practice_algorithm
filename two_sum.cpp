// gitHub URL: https://github.com/userNameWhere/leetCode_practice_algorithm
// an algorithm question from leetcode.com
// question: 1.two sum
// file

#include <iostream> 
#include <vector>     // for using data structore <vector> 
using namespace std;

class Solution {
public:
    vector <int> twoSum(vector<int> nums, int target) {

        // constructor
        vector <int> result;

        for (int i = 0; i < nums.size(); i++) {

            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[i] + nums[j] == target) {
                    result.push_back(i);
                    result.push_back(j);
                    return result;
                }
            }
        }

        return result;
    }
};

int main() {



}