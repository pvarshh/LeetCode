# [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/)

## Topics
- Array
- Prefix Sum


## Description
Given an integer array `nums`, return *an array* `answer` *such that* `answer[i]` *is equal to the product of all the elements of* `nums` *except* `nums[i]`.

The product of any prefix or suffix of `nums` **is guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time without using the division operation.

## Example 1
**Input:** nums = [1,2,3,4]

**Output:** [24,12,8,6]

## Example 2
**Input:** nums = [-1,1,0,-3,3]

**Output:** [0,0,9,0,0] 


## Constraints
- `2 <= nums.length <= 10`<sup>`5`</sup>
- `-30 <= nums[i] <= 30`
- The input is generated such that `answer[i]` **is guaranteed** to fit in a **32-bit** integer.


## Intuition
walk left to right storing product to the left of idx; then walk right to left, multiplying product to the right of idx

## Complexity 
**Time:** O(n) -> linear search across nums to populate left and right 

**Space:** O(n) -> list to store final solution

## Solution
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1] * len(nums)
        
        left = 1
        for i in range(len(nums)):
            product[i] *= left
            left *= nums[i]

        right = 1
        for i in range(len(nums)-1, -1, -1):
            product[i] *= right
            right *= nums[i]
        
        return product
    