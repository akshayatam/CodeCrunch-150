#include <iostream>
#include <algorithm>

using namespace std;

// Utility function to reverse a part of the string in-place
void reverseString(string &s, int start, int end) {
    while (start < end) {
        swap(s[start++], s[end--]);
    }
}

// Function to trim and reduce multiple spaces to a single space in-place
void cleanSpaces(string &s) {
    int n = s.length();
    int i = 0, j = 0;

    while (j < n) {
        // Skip spaces at the beginning
        while (j < n && s[j] == ' ') j++;
        // Copy word
        while (j < n && s[j] != ' ') s[i++] = s[j++];
        // Skip spaces in-between
        while (j < n && s[j] == ' ') j++;
        // Check if we're still within the string and add a space before the next word
        if (j < n) s[i++] = ' ';
    }
    
    s.resize(i); // Resize the string to the new length
}

// Function to reverse words in the string s in-place
void reverseWords(string &s) {
    // Step 1: Reverse the entire string
    reverseString(s, 0, s.length() - 1);

    // Step 2: Reverse each word in the string
    int start = 0, end = 0, n = s.length();
    while (start < n) {
        // Find the start of the next word
        while (start < end || (start < n && s[start] == ' ')) start++;
        // Find the end of the current word
        while (end < start || (end < n && s[end] != ' ')) end++;
        // Reverse the current word
        reverseString(s, start, end - 1);
    }

    // Step 3: Clean up spaces
    cleanSpaces(s);
}

int main() {
    // Example 1
    string example1 = "the sky is blue";
    reverseWords(example1);
    cout << "Example 1 Output: '" << example1 << "'\n";
    
    // Example 2
    string example2 = "  hello world  ";
    reverseWords(example2);
    cout << "Example 2 Output: '" << example2 << "'\n";
    
    // Example 3
    string example3 = "a good   example";
    reverseWords(example3);
    cout << "Example 3 Output: '" << example3 << "'\n";
    
    return 0;
}
