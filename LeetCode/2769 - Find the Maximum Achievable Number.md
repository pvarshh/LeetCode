# [2769. Find the Maximum Achievable Number](https://leetcode.com/problems/find-the-maximum-achievable-number/description/)

## Topics
- Math

## Description
Given two integers, `num` and `t`. A number `x` is **achievable** if it can become equal to `num` after applying the following operation **at most** t times:

- Increase or decrease `x` by 1, and *simultaneously* increase or decrease  `num` by 1.

Return the **maximum** possible value of `x`.

## Example 1
**Input:** num = 4, t = 1

**Output:** 6

**Explanation:**

Apply the following operation once to make the maximum achievable number equal to `num`:
- Decrease the maximum achievable number by 1, and increase `num` by 1.

## Example 2

**Input:** num = 3, t = 2

**Output:** 7

**Explanation:**

Apply the following operation twice to make the maximum achievable number equal to `num`:

- Decrease the maximum achievable number by 1, and increase `num` by 1.


## Constraints
- `1 <= num, t <= 50`


## Intuition
since our goal is to make resulting number max, we should only be going right on the number scale. each operation causes a variance of 2; a +1 and -1, so for each t, we move 2 spaces

## Complexity 
**Time:** O(1) -> trivial

**Space:** O(1) -> trivial

## Solution
```python
class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + t * 2
    