# [1929. Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/description/)

## Topics
- 

## Description


## Example 1
**Input:**  

**Output:** 

**Explanation:** 


## Constraints
- 


## Intuition
simply concatonate the list to itself, can be done by nums * 2 in python

## Complexity 
**Time:** O(1) -> trivial

**Space:** O(1) -> trivial


## Solution
```python
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2
    