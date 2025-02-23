# [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/description/)

## Topics
- Hash Table
- String
- Sorting


## Description
Given two strings `s` and `t`, return `true` if `t` is an  [anagram](https://www.merriam-webster.com/dictionary/anagram) of `s`, and `false` otherwise.


## Example 1
**Input:**  s = "anagram", t = "nagaram"

**Output:** true

## Example 2
**Input:**  s = "rat", t = "car"

**Output:** false


## Constraints
- `1 <= s.length, t.length <= 5 * 104`
- `s` and `t` consist of lowercase English letters.

## Intuition
use a map to store the frequecncy of characters. increment when seen in s; decrement when seen in t. return true if resulting map is 0, else return false

## Complexity 
**Time:** O(n) -> loop across s and t to update map

**Space:** O(1) -> constant size map of 26 (all lower characters)

## Solution
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = [0] * 26
        for c in s:
            counts[ord(c) - ord('a')] += 1
        for c in t:
            counts[ord(c) - ord('a')] -= 1
        return all(count == 0 for count in counts)