#include <iostream>
#include <string>  // Include the string library

using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        
        // Convert integer to string
        string number1 = to_string(x);

        // Check for palindrome
        int n = number1.length();

        for (int i = 0; i < n /2; i++) {
            if (number1[i] != number1[n - i - 1]) {
                return false; // If mismatch found, it's not a palindrome
            }
        }

        return true; // If no mismatches, it's a palindrome
    }
};

int main() {

    // initialize a solution
    Solution solution;

    cout << solution.isPalindrome(1221);

}


