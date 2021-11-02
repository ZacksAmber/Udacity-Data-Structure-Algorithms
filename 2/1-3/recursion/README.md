# Recursion

## Basic

### [Recursion Introduction](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/recursion/introduction.ipynb)

---

### [Factorial using recursion](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/recursion/Factorial%20using%20recursion.ipynb)

---

### [Reversing a String](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/recursion/Reversing%20a%20string.ipynb)

---

### [Palindrome](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/recursion/Checking%20Palindrome.ipynb)

A **palindrome** is a word that is the reverse of itself—that is, it is the same word when read forwards and backwards.

For example:
*  "madam" is a palindrome
* "abba" is a palindrome
*  "cat" is not
*  "a" is a trivial case of a palindrome

The goal of this exercise is to use recursion to write a function `is_palindrome` that takes a string as input and checks whether that string is a palindrome. (Note that this problem can also be solved with a non-recursive solution, but that's not the point of this exercise.)

---

### [Add One](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/recursion/Add-One-Again.ipynb)

---

## Advanced

### [List Permutation](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/recursion/Permutation.ipynb)

<mark>Hard</mark>

---

### [String Permutation](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/recursion/String-Permutations.ipynb)

<mark>Hard</mark>

<mark>Unfinished</mark>

---

### [Keypad Combinations](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/recursion/Keypad%20Combinations.ipynb)

A keypad on a cellphone has alphabets for all numbers between 2 and 9, as shown in the figure below:

<img style="float: center;height:200px;" src="Keypad.png" alt="A cell phone keypad that has letters associated with each number 2 through 9"><br>

You can make different combinations of alphabets by pressing the numbers.

For example, if you press 23, the following combinations are possible:

`ad, ae, af, bd, be, bf, cd, ce, cf`

Note that because 2 is pressed before 3, the first letter is always an alphabet on the number 2.
Likewise, if the user types 32, the order would be

`da, db, dc, ea, eb, ec, fa, fb, fc`


Given an integer `num`, find out all the possible strings that can be made using digits of input `num`. 
Return these strings in a list. The order of strings in the list does not matter. However, as stated earlier, the order of letters in a particular string matters.

<mark>Hard</mark>

<mark>Unfinished</mark>

---

### [Deep Reverse](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/recursion/Deep%20Reverse.ipynb)

Define a procedure, `deep_reverse`, that takes as input a list, and returns a new list that is the deep reverse of the input list.  
This means it reverses all the elements in the list, and if any of those elements are lists themselves, reverses all the elements in the inner list, all the way down. 

>Note: The procedure must not change the input list itself.

**Example**<br>
Input: `[1, 2, [3, 4, 5], 4, 5]`<br>
Output: `[5, 4, [5, 4, 3], 2, 1]`<br>

**Hint**<br>
1. Begin with a blank final list to be returned.
2. Traverse the given list in the reverse order.
 * If an item in the list is a list itself, call the same function.
 * Otheriwse, append the item to the final list.


---

### [Call stack](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/recursion/Call%20stack.ipynb)

---

### [Recurrence Relations](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/recursion/Recurrence%20Relations.ipynb)

Binary Search

---

### [Tower of Hanoi](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/recursion/Tower-of-Hanoi.ipynb)

The Tower of Hanoi is a puzzle where we have three rods and `n` unique sized disks. The three rods are - source, destination, and auxiliary as shown in the figure below.
<br><img style="float: center;" src="TOH.png" alt="Image of 3 rod with all disks on the leftmost tower and instructions to move them to the rightmost tower."><br>
Initally, all the `n` disks are present on the source rod. The final objective of the puzzle is to move all disks from the source rod to the destination rod using the auxiliary rod.<br><br> 
**However, there are some rules applicable to all rods:**
    1. Only one disk can be moved at a time.
    2. A disk can be moved only if it is on the top of a rod.
    3. No disk can be placed on the top of a smaller disk.
    
You will be given the number of disks `num_disks` as the input parameter. Write a **recursive function** `tower_of_Hanoi()` that prints the "move" steps in order to move `num_disks` number of disks from Source to Destination using the help of Auxiliary rod.

---

#### Example Illustration
For example, if you have `num_disks = 3`, then the disks should be moved as follows:
    
        1. move disk from source to destination
        2. move disk from source to auxiliary
        3. move disk from destination to auxiliary
        4. move disk from source to destination
        5. move disk from auxiliary to source
        6. move disk from auxiliary to destination
        7. move disk from source to destination
        
You must print these steps as follows:    

                S D
                S A
                D A
                S D
                A S
                A D
                S D
        
Where S = source, D = destination, A = auxiliary <br><br>
An example illustration for `num_disks = 4` can be visualized in this [GIF from wikipedia](https://en.wikipedia.org/wiki/Tower_of_Hanoi#/media/File:Tower_of_Hanoi_4.gif)


<mark>Hard</mark>

<mark>Unfinished</mark>

---

### [Return Codes](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/recursion/Return-Codes.ipynb)

In an encryption system where ASCII lower case letters represent numbers in the pattern `a=1, b=2, c=3...` and so on, find out all the codes that are possible for a given input number. 

**Example 1**

* `number = 123`
* `codes_possible = ["aw", "abc", "lc"]`

Explanation: The codes are for the following number:
         
* 1 . 23     = "aw"
* 1 . 2 . 3  = "abc"
* 12 . 3     = "lc"
    

**Example 2**  

* `number = 145`
* `codes_possible = ["ade", "ne"]`

Return the codes in a list. The order of codes in the list is not important.

*Note: you can assume that the input number will not contain any 0s*

<mark>Hard</mark>

---

### [Return Subsets](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/recursion/Return-Subsets.ipynb)

Given an integer array, find and return all the subsets of the array.
The order of subsets in the output array is not important. However the order of elements in a particular subset should remain the same as in the input array.

**Note**: 
- An empty set will be represented by an empty list.
- If there are repeat integers, each occurrence must be treated as a separate entity.

**Example 1**

```
arr = [9, 9]

output = [[],
          [9],
          [9],
          [9, 9]]
```

**Example 2**

```
arr = [9, 12, 15]

output =  [[],
           [15],
           [12],
           [12, 15],
           [9],
           [9, 15],
           [9, 12],
           [9, 12, 15]]
```

---

### [Staircase](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/recursion/Staircase.ipynb)

Suppose there is a staircase that you can climb in either 1 step, 2 steps, or 3 steps. In how many possible ways can you climb the staircase if the staircase has `n` steps? Write a recursive function to solve the problem.

**Example:**

* `n == 1` then `answer = 1`

* `n == 3` then `answer = 4`<br>
   The output is `4` because there are four ways we can climb the staircase:
    - 1 step +  1 step + 1 step
    - 1 step + 2 steps 
    - 2 steps + 1 step
    - 3 steps
* `n == 5` then `answer = 13`

> [Mathematical induction](https://en.wikipedia.org/wiki/Mathematical_induction#Description)

> [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)
> [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
> [1137. N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/)

---

### [Last Index](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/recursion/Last-index-recursion.ipynb)

Given an array `arr` and a target element `target`, find the last index of occurence of `target` in `arr` using recursion. If `target` is not present in `arr`, return `-1`.

For example:

1. For `arr = [1, 2, 5, 5, 1, 2, 5, 4]` and `target = 5`, `output = 6`

2. For `arr = [1, 2, 5, 5, 1, 2, 5, 4]` and `target = 7`, `output = -1`