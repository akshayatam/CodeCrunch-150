#include <iostream>
#include <numeric> // For std::gcd
using namespace std;

class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        // Check if str1 and str2 are concatenations of some common substring
        if (str1 + str2 == str2 + str1) {
            // Calculate the GCD of the lengths of str1 and str2
            int gcdLen = gcd(str1.length(), str2.length());
            // Return the largest common substring that divides both str1 and str2
            return str1.substr(0, gcdLen);
        } else {
            // Return an empty string if no common dividing substring is found
            return "";
        }
    }
};

int main() {
    Solution solution;
    // Example 1
    cout << solution.gcdOfStrings("ABCABC", "ABC") << endl;  // Output: "ABC"
    // Example 2
    cout << solution.gcdOfStrings("ABABAB", "ABAB") << endl; // Output: "AB"
    // Example 3
    cout << solution.gcdOfStrings("LEET", "CODE") << endl;   // Output: ""
    return 0;
}
