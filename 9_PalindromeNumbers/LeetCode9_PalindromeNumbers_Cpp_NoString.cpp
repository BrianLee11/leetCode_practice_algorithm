#include <iostream>

using namespace std;

class Solution {
public:
    bool isPalindrome(int number) {

        // trivial case 1: if negative number, then false
        if (number < 0) return false;

        // trivial case 2: if single number, then true
        if (number / 10 == 0) return true;

        // non-trival case
        
        // save the integer
        int number1 = number;

        // initialize variables
        int divisor = 1;

        // compute the number of digits
        while (number1 / 10 != 0) {
            divisor *= 10;
            number1 = number1 / 10;
        }

        // check palindrome
        while (number != 0) {
            int last_digit = number % 10;       // remainder
            int first_digit = number / divisor; // quotient
            
            if (last_digit != first_digit) return false; // not palindrome
            
            number = (number % divisor) / 10; // Remove the first and last digits from the number
            divisor = divisor / 100; // Update the divisor
        }

        return true; // The number is a palindrome if all digit comparisons passed
    }
};

int main() {
    Solution solution;
    cout << solution.isPalindrome(121) << endl;
    cout << solution.isPalindrome(-121) << endl;
    cout << solution.isPalindrome(0) << endl;
};
