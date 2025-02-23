# [128. Longest Consecutive Sequencee](https://leetcode.com/problems/longest-consecutive-sequence/description/)

## Topics
- Array
- Hash Table
- Union Find

## Description
Given an unsorted array of integers `nums`, return *the length of the longest consecutive elements sequence*.

You must write an algorithm that runs in `O(n)` time.



## Example 1
**Input:** nums = [100,4,200,1,3,2]

**Output:** 4

**Explanation:** The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

## Example 2
**Input:** nums = [0,3,7,2,5,8,4,6,0,1]

**Output:** 9

## Example 3
**Input:** nums = [1,0,1,2]

**Output:** 3


## Constraints
- `0 <= nums.length <= 10`<sup>`5`</sup>
-  `-10`<sup>`9`</sup> `<= nums[i] <= 10`<sup>`9`</sup>


## Intuition
store the nums into a setfor easy access. iterate across the set, find length of sequence if num is start of sequence by incrementing by length until num+length not in set. set max_length as max if itself and length of current sequence

## Complexity 
**Time:** O(n) -> only explore sequence if num is start

**Space:** O(n) -> store nums into a set

## Solution
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = set(nums)
        max_length = 1
        for num in nums:
            if num-1 not in nums:
                length = 1
                while num+length in nums:
                    length += 1
                max_length = max(max_length, length)
        return max_length

    