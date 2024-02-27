#include <iostream>
#include <vector>
#include <algorithm> // Include for max_element
using namespace std;

class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        // Find the maximum number of candies any kid currently has
        int max_candies = *max_element(candies.begin(), candies.end());
        
        // Initialize a vector to store the result
        vector<bool> result;
        
        // Iterate over each kid
        for (int c : candies) {
            // Check if adding extraCandies makes the kid have the greatest number of candies
            result.push_back(c + extraCandies >= max_candies);
        }
        
        // Return the result vector
        return result;
    }
};

// Main function to test the solution with provided examples
int main() {
    Solution sol;
    vector<int> candies1 = {2,3,5,1,3};
    vector<int> candies2 = {4,2,1,1,2};
    vector<int> candies3 = {12,1,12};
    
    // Example 1
    vector<bool> result1 = sol.kidsWithCandies(candies1, 3);
    for (bool b : result1) cout << (b ? "true" : "false") << " ";
    cout << endl;
    
    // Example 2
    vector<bool> result2 = sol.kidsWithCandies(candies2, 1);
    for (bool b : result2) cout << (b ? "true" : "false") << " ";
    cout << endl;
    
    // Example 3
    vector<bool> result3 = sol.kidsWithCandies(candies3, 10);
    for (bool b : result3) cout << (b ? "true" : "false") << " ";
    cout << endl;
    
    return 0;
}
