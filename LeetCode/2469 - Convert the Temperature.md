# [2469. Convert the Temperature](https://leetcode.com/problems/convert-the-temperature/description/)

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
simply do the math in the problem description, returing a list of [kelvin, fahrenheit]

## Complexity 
**Time:** O(1) -> trivial

**Space:** O(1) -> trivial

## Solution
```python
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.80 + 32.00]