#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    // canPlaceFlowers determines if n new flowers can be planted in the flowerbed
    // without violating the no-adjacent-flowers rule.
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        // Initialize flag to indicate if the previous plot has a flower.
        bool flag = flowerbed[0] ? true : false;

        // Iterate through the flowerbed to find spots for new flowers.
        for (int i = 0; i < flowerbed.size() - 1; ++i) {
            // Check if current and next plots are empty and we didn't plant a flower just before.
            if (flowerbed[i] == 0 && flowerbed[i + 1] == 0 && !flag) {
                n--;        // Plant a flower.
                flag = true; // Update flag since we just planted a flower.
            } else if (flowerbed[i] == 0) {
                flag = false; // Current plot is empty, and we didn't plant a flower.
            } else {
                flag = true; // Current plot is not empty.
            }
        }

        // Consider the last plot separately.
        if (!flag && flowerbed.back() == 0) {
            n--; // Plant a flower if possible.
        }

        // If n is 0 or negative, it means all flowers can be planted.
        return n <= 0;
    }
};

int main() {
    Solution sol;
    vector<int> flowerbed1 = {1, 0, 0, 0, 1};
    cout << boolalpha << sol.canPlaceFlowers(flowerbed1, 1) << endl; // Expected output: true

    vector<int> flowerbed2 = {1, 0, 0, 0, 1};
    cout << boolalpha << sol.canPlaceFlowers(flowerbed2, 2) << endl; // Expected output: false

    return 0;
}
