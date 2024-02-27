#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

// Function to reverse words in a string
string reverseWords(string s) {
    stringstream ss(s);
    string word;
    vector<string> words;
    
    // Extract words from the stream and push into vector
    while(ss >> word) {
        words.push_back(word);
    }
    
    // Reverse the vector of words
    reverse(words.begin(), words.end());
    
    // Join the words back into a single string
    string result;
    if(!words.empty()) {
        result += words[0];
    }
    for(size_t i = 1; i < words.size(); ++i) {
        result += " " + words[i];
    }
    
    return result;
}

int main() {
    // Example 1
    string example1 = "the sky is blue";
    cout << "Input: '" << example1 << "'\nOutput: '" << reverseWords(example1) << "'\n";
    
    // Example 2
    string example2 = "  hello world  ";
    cout << "\nInput: '" << example2 << "'\nOutput: '" << reverseWords(example2) << "'\n";
    
    // Example 3
    string example3 = "a good   example";
    cout << "\nInput: '" << example3 << "'\nOutput: '" << reverseWords(example3) << "'\n";
    
    return 0;
}
