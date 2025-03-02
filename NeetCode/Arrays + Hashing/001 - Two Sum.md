# [1. Two Sum](https://leetcode.com/problems/two-sum/description/)

## Topics
- Array
- Hash Table

## Description
Given an array of integers nums and an integer `target`, return *indices* of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the *same* element twice.

You can return the answer in any order.

## Example 1
**Input:**  nums = [2,7,11,15], target = 9

**Output:** [0,1]

**Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1].

## Example 2
**Input:**  nums = [3,2,4], target = 6

**Output:** [1,2]

## Example 3: 
**Input:** nums = [3,3], target = 6

**Output:** [0,1]

## Constraints
- `2 <= nums.length <= 104`
- `-10`<sup>`9`</sup>`<= nums[i] <= 109`
- `-10`<sup>`9`</sup>`<= target <= 109`
- Only one valid answer exists.

## Intuition
use a map to store num and its idx. loop across nums, checking if complement (target - num) exists in map. if exists, return complement's idx and curr idx; else continue

## Complexity 
**Time:** O(n) -> linear search across nums

**Space:** O(n) -> store idx, num in map

## Solution
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [idx, seen[complement]]
            seen[num] = idx
        return []