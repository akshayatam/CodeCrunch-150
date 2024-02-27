#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    // Function to merge strings alternately
    string mergeAlternately(string word1, string word2) {
        // Get the lengths of word1 and word2
        int n = word1.size();
        int m = word2.size();
        // Initialize an empty string to store the merged result
        string ans = "";

        // Iterate over the characters of both strings up to the minimum length
        for (int i = 0; i < n && i < m; ++i) {
            // Append characters alternately from word1 and word2
            ans += word1[i];
            ans += word2[i];
        }

        // If word1 is longer than word2, append the remaining characters of word1
        if (n > m) {
            ans += word1.substr(m);
        } else if (n < m) { // If word2 is longer than word1, append the remaining characters of word2
            ans += word2.substr(n);
        }

        return ans;
    }
};

int main() {
    // Test cases
    Solution solution;

    string word1 = "abc";
    string word2 = "pqr";
    cout << "Example 1:" << endl;
    cout << "Input: " << word1 << ", " << word2 << endl;
    cout << "Output: " << solution.mergeAlternately(word1, word2) << endl; // Expected output: "apbqcr"

    word1 = "ab";
    word2 = "pqrs";
    cout << "\nExample 2:" << endl;
    cout << "Input: " << word1 << ", " << word2 << endl;
    cout << "Output: " << solution.mergeAlternately(word1, word2) << endl; // Expected output: "apbqrs"

    word1 = "abcd";
    word2 = "pq";
    cout << "\nExample 3:" << endl;
    cout << "Input: " << word1 << ", " << word2 << endl;
    cout << "Output: " << solution.mergeAlternately(word1, word2) << endl; // Expected output: "apbqcd"

    return 0;
}
