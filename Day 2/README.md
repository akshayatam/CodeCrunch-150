# **Day 2: Streak Started**

On the second day of our coding adventure, where we have the following problems: **Can Place Flowers**, **Reverse Vowels of a String**, and **Reverse Words in a String**.

---

## 1. Can Place Flowers (Problem link [here](https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75))
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in **adjacent** plots.

Given an integer array `flowerbed` containing `0`'s and `1`'s, where `0` means empty and `1` means not empty, and an integer `n`, return `true` *if `n` new flowers can be planted in the `flowerbed` without violating the no-adjacent-flowers rule and `false` otherwise.*

**Example 1**
```
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
```

**Example 2**
```
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
```

**Constraints**
- `1 <= flowerbed.length <= 2 * 10^4`
- `flowerbed[i]` is `0` or `1`.
- There are no two adjacent flowers in `flowerbed`.
- `0 <= n <= flowerbed.length`

---

## 2. Reverse Vowels of a String (Problem link [here](https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75))
Given a string s, reverse only all the vowels in the string and return it.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in both lower and upper cases, more than once.

***Example 1**
```
Input: s = "hello"
Output: "holle"
```
**Example 2**
```
Input: s = "leetcode"
Output: "leotcede"
```

**Constraints:**

- `1 <= s.length <= 3 * 10^5`
- `s` consist of printable ASCII characters.

---

## 3. Reverse Words in a String (Problem link [here](https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75))
Given an input string `s`, reverse the order of the words.

A word is defined as a sequence of non-space characters. The **words** in `s` will be separated by at least one space.

Return *a string of the words in reverse order concatenated by a single space.*

**Note:** `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


**Example 1**
```
Input: s = "the sky is blue"
Output: "blue is sky the"
```
**Example 2**
```
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
```
**Example 3**
```
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
```

**Constraints**

- `1 <= s.length <= 10^4`
- `s` contains English letters (upper-case and lower-case), digits, and spaces `' '`.
- There is **at least one** word in `s`.

**Follow-up:** If the string data type is mutable in your language, can you solve it in-place with `O(1)` extra space?
