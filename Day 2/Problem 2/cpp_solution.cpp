#include <iostream>
#include <algorithm>
#include <set>
using namespace std;

class Solution {
public:
    string reverseVowels(string s) {
        set<char> vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        int left = 0, right = s.length() - 1;

        while (left < right) {
            // Find the next vowel from the left
            while (left < right && vowels.find(tolower(s[left])) == vowels.end()) {
                left++;
            }
            // Find the next vowel from the right
            while (left < right && vowels.find(tolower(s[right])) == vowels.end()) {
                right--;
            }

            // Swap the vowels
            swap(s[left], s[right]);
            left++;
            right--;
        }

        return s;
    }
};

int main() {
    Solution solution;
    cout << solution.reverseVowels("hello") << endl;    // Output: "holle"
    cout << solution.reverseVowels("leetcode") << endl; // Output: "leotcede"

    return 0;
}
