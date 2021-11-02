# Array

## Basic

### [Add-One](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/arrays/Add-One.ipynb)

You are given a non-negative number in the form of list elements. For example, the number `123` would be provided as `arr = [1, 2, 3]`. Add one to the number and return the output in the form of a new list. 

**Example 1:**
* `input = [1, 2, 3]`
* `output = [1, 2, 4]`


**Example 2:**
* `input = [1, 2, 9]`
* `output = [1, 3, 0]`

**Example 3:**
* `input = [9, 9, 9]`
* `output = [1, 0, 0, 0]`


**Challenge:**
One way to solve this problem is to convert the input array into a number and then add one to it. For example, if we have `input = [1, 2, 3]`, you could solve this problem by creating the number `123` and then separating the digits of the output number `124`.

But can you solve it in some other way?

---

### [Duplicate Number](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/arrays/Duplicate-Number.ipynb)

You have been given an array of `length = n`. The array contains integers from `0` to `n - 2`. Each number in the array is present exactly once except for one number which is present twice. Find and return this duplicate number present in the array

**Example:**
* `arr = [0, 2, 3, 1, 4, 5, 3]`
* `output = 3` (because `3` is present twice)

The expected time complexity for this problem is `O(n)` and the expected space-complexity is `O(1)`.

---

### [Max Sum Subarray](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/arrays/Max-Sum-Subarray.ipynb)

You have been given an array containg numbers. Find and return the largest sum in a contiguous subarray within the input array.

**Example 1:**
* `arr= [1, 2, 3, -4, 6]`
* The largest sum is `8`, which is the sum of all elements of the array.

**Example 2:**
* `arr = [1, 2, -5, -4, 1, 6]`
* The largest sum is `7`, which is the sum of the last two elements of the array.

---

### [Pascal's-Triangle](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/arrays/Pascal's-Triangle.ipynb)

Find and return the `nth` row of Pascal's triangle in the form a list. `n` is 0-based.

For example, if `n = 4`, then `output = [1, 4, 6, 4, 1]`.

To know more about Pascal's triangle: https://www.mathsisfun.com/pascals-triangle.html