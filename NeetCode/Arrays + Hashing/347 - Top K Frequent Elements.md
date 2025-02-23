# [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/)

## Topics
- Array
- Hash Table
- Divide and Conquer
- Sorting
- Heap (Priority Queue)
- Bucket Sort
- Counting
- Quickselect

## Description
Given an integer array `nums` and an integer `k`, return the `k` *most frequent* elements. You may return the answer in any order.

## Example 1
**Input:**  nums = [1,1,1,2,2,3], k = 2
**Output:** [1,2]

## Example 2
**Input:**  nums = [1], k = 1
**Output:** [1]

## Constraints
- `1 <= nums.length <= 10`<sup>`5`</sup>
- `-10`<sup>`4`</sup> `<= nums[i] <= 104`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is guaranteed that the answer is unique.

## Intuition
initialize and populate a frequency map. notice worst case if all num in nums are same, we would have counter[num] = len(nums), so initialize our bucket collection with len(num)+1. populate buckets based of freq of num; iterate backwards until k elements are seen, then return

## Complexity 
**Time:** O(n) -> loop across nums to populate counter

**Space:** O(n) -> create a counter dict to hold the frequencies

## Solution
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1
        
        freqs = [[] for _ in range(len(nums) + 1)]
        for num, freq in counter.items():
            freqs[freq].append(num)

        result = []
        for i in range(len(freqs) - 1, -1, -1):
            for num in freqs[i]:
                result.append(num)
                if len(result) == k:
                    return result