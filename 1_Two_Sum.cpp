/* Created by : Brian J.Lee
- creation date: August 9, 2023
- gitHub URL: https://github.com/userNameWhere/leetCode_practice_algorithm
- an algorithm question from leetcode.com
- question: 1.two sum
- file name: 1_Two_Sum.cpp
- purpose of this file: 1) solve algorithm, 2) review basic grammar of C++
*/

#include <iostream>   
/*
* This header file is part of the Standard Library and provides declarations for
input and output stream-related classes and objects.
*/

#include <vector>     // allows the data structore <vector> 
/*
The <vector> header provides the implementation of the std::vector class template, 
which represents a dynamic array that can grow or shrink in size as elements 
are added or removed.
*/


using namespace std;  
/*  
* this statement is used to bring all the symbols 
(functions, classes, objects, etc.) 
from the Standard Library into the current scope, making them accessible without 
needing to prefix them with std::.
Example: rather than std::cout, just use cout
*/

/* 
* Use "class" to practice object-oriented-programming(OOP)
*/

class Solution {
public:
    vector <int> twoSum(vector<int> nums, int target) {

        // constructor
        // Declare a vector to store the result indices
        vector <int> result;

        // Iterate through the vector using nested loops
        for (int i = 0; i < nums.size(); i++) {

            for (int j = i + 1; j < nums.size(); j++) {
                // Check if the sum of elements at indices i and j is equal to target
                if (nums[i] + nums[j] == target) {
                    result.push_back(i); // Push the indices to the result vector
                    result.push_back(j);
                    return result; // Return the result vector and exit the function
                }
            }
        }

        // If no such pair is found, an empty result vector is returned
        return result;
    }
};

// declare a function
void printVector(vector <int> result);

int main() {

    Solution solution;

    // example 1
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;

    vector<int> result = solution.twoSum(nums, target);
    printVector(result);

    // example 2
    nums = {3,2,4};
    target = 6;

    result = solution.twoSum(nums, target);
    printVector(result);


    // example 3
    nums = {3,3};
    target = 6;

    result = solution.twoSum(nums, target);
    printVector(result);

    
    return 0;
}

// define function
void printVector(vector <int> result) {

    // display elements
    cout << "Output: [";
    for (int i = 0; i < result.size(); i++) {

        if (i != result.size() - 1) {
            cout << result[i] << ", ";
        }
        else {
            cout << result[i];
        }
    }
    cout << "]" << endl;
}

