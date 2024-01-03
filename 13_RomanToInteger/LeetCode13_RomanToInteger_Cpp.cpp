/*
LeetCode
Problem 13: Roman to Integer
Written in C++
*/


#include <iostream>
using namespace std;

class Solution {
public:
    int romanToInt(string s) {

        // initialize variables
        int number = 0;
        int i = 0;

        while (i < s.length()) {

            // case 1: starts with I
            if (s[i] == 'I') {
                // checking for IV or IX
                // check validity
                if (i + 1 < s.length()) {
                    if (s[i + 1] == 'V') {
                        number += 4; // IV = 4
                        i += 2;      // jump index by 2, not 1
                        continue;    // continue in the while loop
                    }
                    else if (s[i + 1] == 'X') {
                        number += 9; // IX = 9
                        i += 2;
                        continue;
                    }
                    else number += 1; // at least two digits remain, but not IV nor IX
                }
                // not the case of IV nor IX
                else number += 1; 
            } // end of case 1: I

            // case 2: starts with X 
            else if (s[i] == 'X') {
                // checking for XL or XC
                // check validity
                if (i + 1 < s.length()) {
                    if (s[i + 1] == 'L') {
                        number += 40;
                        i += 2;
                        continue;
                    }

                    else if (s[i + 1] == 'C') {
                        number += 90;
                        i += 2;
                        continue;
                    }
                    else number += 10; 
                }
                // not XL nor XC
                else number += 10;
            } // end of case 2: X

            // case 3: start with C
            else if (s[i] == 'C') {
                // check for CD or CM
                // check for validity
                if (i + 1 < s.length()) {

                    if (s[i + 1] == 'D') {
                        number += 400;
                        i += 2;
                        continue;
                    }

                    else if (s[i + 1] == 'M') {
                        number += 900;
                        i += 2;
                        continue;
                    }

                    // two digit, but not CD nor CM
                    else number += 100;
                }

                // not two digit
                else number += 100;
            } // end of case 3: C


            // Single character cases
            else if (s[i] == 'V') number += 5;
            else if (s[i] == 'L') number += 50;
            else if (s[i] == 'D') number += 500;
            else if (s[i] == 'M') number += 1000;

            // increment index by 1 for not IV, IX, XL, XC, CD, CM
            i += 1;

            cout << number << endl;

        } // end of while


    return number;
  
} // end of function

};


int main() {

    Solution solution;



    int result = solution.romanToInt("DCXXI");
    cout << result << endl; // output: 641. but should be 621



    //int result = solution.romanToInt("III");
    //cout << result << endl; 

    //result = solution.romanToInt("LVIII");
    //cout << result << endl;

    //result = solution.romanToInt("MCMXCIV");
    //cout << result << endl;
      
}
