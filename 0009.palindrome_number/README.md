# 0009. Palindrome Number

![Static Badge](https://img.shields.io/badge/Level-Easy-42c6c2)

## I. Problem:

Given an integer `x`, return `true` _if `x` is a <span style="color:#0a83fe">
**palindrome**</span>, and `false` otherwise_.

### Constraints:

- -2<sup>31</sup> <= x <= 2<sup>31</sup> - 1

## II. Examples:

### Example 1:

> **Input:** x = 121  
> **Output:** true  
> **Explanation:** 121 reads as 121 from left to right and from right to left.

### Example 2:

> **Input:** x = -121  
> **Output:** false  
> **Explanation:** From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

### Example 3:

> **Input:** x = 10  
> **Output:** false  
> **Explanation:** Reads 01 from right to left. Therefore it is not a palindrome.

## III. Solution

- We simply divide the input number into 2 symmetrical parts. In turn, we compare the numbers from front to back of the 1st part with the numbers from back to front of the 2nd part. If every pair of the comparison is the same, return `True`.
  <div align="center" style="margin-bottom:6px">
    <img src="./assets/img-0009-001.svg" loading="lazy" width=30%>
  </div>
- If any pair of the comparison is not the same, return `False`.
  <div align="center" style="margin-bottom:6px">
    <img src="./assets/img-0009-002.svg" loading="lazy" width=30%>
  </div align="center">
