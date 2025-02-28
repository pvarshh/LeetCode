# [1920. Build Array from Permutation](link)

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
follow the description, so ans[i] = nums[nums[i]]

## Complexity 
**Time:** O(n) -> loop across nums to build ans

**Space:** O(n) -> extra space for ans 


## Solution
```python
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        for idx, num in enumerate(nums):
            ans[idx] = nums[num]
        return ans
    