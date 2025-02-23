# [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/description/)

## Topics
- Array
- Hash Table
- String
- Sorting

## Description
Given an array of strings `strs`, group the 
[anagrams](https://www.merriam-webster.com/dictionary/anagram) together. You can return the answer in **any** order.

## Example 1
**Input:** strs = ["eat","tea","tan","ate","nat","bat"]

**Output:** [["bat"],["nat","tan"],["ate","eat","tea"]]

**Explanation:**
- There is no string in strs that can be rearranged to form `"bat"`.
- The strings `"nat"` and `"tan"` are anagrams as they can be rearranged to form each other.
- The strings `"ate"`, `"eat"`, and `"tea"` are anagrams as they can be rearranged to form each other.

## Example 2

**Input:** strs = [""]

**Output:** [[""]]

## Example 3

**Input:** strs = ["a"]

**Output:** [["a"]]

## Constraints
- `1 <= strs.length <= 10`<sup>`4`</sup>
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.


## Intuition
map the frequency of the string to the actual string. if frequency exists in map, append string; else, create new k/v

## Complexity 
**Time:** O(n * k) -> linear search across the strings, linear search across each string in strings to populate the map

**Space:** O(n) -> store every map (O(26)) as the key, and strings as the values


## Solution
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for anagram_value in strs:
            anagram_key = [0] * 26
            for char in anagram_value:
                anagram_key[ord(char) - ord('a')] += 1
            anagram_key = tuple(anagram_key)
            if anagram_key in anagram_map:
                anagram_map[anagram_key].append(anagram_value)
            else:
                anagram_map[anagram_key] = [anagram_value]
        return list(anagram_map.values())