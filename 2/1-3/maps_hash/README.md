# Hashmap

## Map

### [Exploring the Map Concepts](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/maps_hash/Introduction%20to%20Maps.ipynb)

---

## HashMap

### [HashMap Introduction](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/maps_hash/HashMap.ipynb)

> [706. Design HashMap](https://leetcode.com/problems/design-hashmap/)


<mark>Hard</mark>

---

### [Caching](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/maps_hash/Caching.ipynb)

A child is running up a staircase and can hop either 1 step, 2 steps or 3 steps at a time. 
Given that the staircase has a total `n` steps, write a function to count the number of possible ways in which child can run up the stairs. 

For e.g. 

* `n == 1` then `answer = 1`

* `n == 3` then `answer = 4`<br>
   The output is `4` because there are four ways we can climb the staircase:
    - 1 step +  1 step + 1 step
    - 1 step + 2 steps 
    - 2 steps + 1 step
    - 3 steps
 
* `n == 5` then `answer = 13`

**Hint**<br>
You would need to make use of the [Inductive Hypothesis](https://en.wikipedia.org/wiki/Mathematical_induction#Description), which comprises of the following two steps:
1. **The Inductive Hypothesis**: Calculate/assume the results for base case. In our problem scenario, the base cases would be when n = 1, 2, and 3. 


2. **The Inductive Step**: Prove that for every $n >= 3$, if the results are true for $n$ , then it holds for $(n+1)$ as well. In other words, assume that the statement holds for some arbitrary natural number $n$ , and prove that the statement holds for $(n+1)$.

---

### [String Key Hash Table](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/maps_hash/String%20Key%20Hash%20Table.ipynb)

- `store()` - a function that takes a string as input, and stores it into the hash table.
- `lookup()` - a function that checks if a string is already available in the hash table. If yes, return the hash value, else return -1.
- `calculate_hash_value()` - a helper function to calculate a hash value of a given string.

---

### [Practice: Pair Sum to Target](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/maps_hash/Pair-Sum-to-target.ipynb)

> [1. Two Sum](https://leetcode.com/problems/two-sum/)

---

### [Longest Consecutive Subsequence](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/maps_hash/Longest-Consecutive-Subsequence.ipynb)

> [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)
> [674. Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/)
> [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)

<mark>Hard</mark>

<mark>Unfinished</mark>
