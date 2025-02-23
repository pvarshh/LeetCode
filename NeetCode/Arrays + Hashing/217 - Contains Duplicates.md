# [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/)

## Topics
- two pointers
- string
- string matching

## Description
given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

## Example 1
**Input:**  haystack = "sadbutsad", needle = "sad"

**Output:**  0

**Explanation:** "sad" occurs at index 0 and 6. The first occurrence is at index 0, so we return 0.

## Example 2
**Input:**  "leetcode", needle = "leeto"

**Output:**  -1

**Explanation:**  "leeto" did not occur in "leetcode", so we return -1.


## Constraints
- `1 <= haystack.length, needle.length <= 104`
- `haystack` and `needle` consist of only lowercase English characters.

## Intuition
use a sliding window of subtring across haystack of len(needle). if the substring is the same as needle, return the current index; else, continue

## Complexity ##
**Time:** O(n) -> loop across haystack once

**Space:** O(1) -> maintain one substring of the current window you are at



## Solution
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
            return i
       return -1