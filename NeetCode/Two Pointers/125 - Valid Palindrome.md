# [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/description/)

## Topics
- Two Pointers
- String

## Description
A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` *if it is a **palindrome**, or* `false` *otherwise*.

## Example 1
**Input:** s = "A man, a plan, a canal: Panama"
**Output:** true
**Explanation:** "amanaplanacanalpanama" is a palindrome.

## Example 2
**Input:** s = "race a car"
**Output:** false
**Explanation:** "raceacar" is not a palindrome.

## Example 3
**Input:** s = " "
**Output:** true
**Explanation:** s is an empty string "" after removing non-alphanumeric characters. Since an empty string reads the same forward and backward, it is a palindrome.

## Constraints
- `1 <= s.length <= 2 * 10`<sup>`5`</sup>
- `s` consists only of printable ASCII characters.


## Intuition
convert to lowercase for ease, then simply walk a pointer from left and right, passing if not alphanumeric and checking for equivalence if alphanum

## Complexity 
**Time:** O(n) -> linearly walk the l and r points across s

**Space:** O(1) -> constant l and r variables to store the pointer index

## Solution
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s)-1
        while l <= r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True