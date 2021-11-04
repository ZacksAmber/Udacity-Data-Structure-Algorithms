# Stack

## Referencecs

> [How to Implement a Python Stack](https://realpython.com/how-to-implement-python-stack/)

---

## Basic

### [Implement a Stuck Using an Array](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/stack/Implement%20a%20stack%20using%20an%20array.ipynb)

- `push` - adds an item to the top of the stack
- `pop` - removes an item from the top of the stack (and returns the value of that item)
- `size` - returns the size of the stack
- `top` - returns the value of the item at the top of stack (without removing that item)
- `is_empty` - returns `True` if the stack is empty and `False` otherwise

---

### [Implement a stack using a Python List](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/stack/python_stack_practice.ipynb)

---

### [Implement a stack using a linked list](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/stack/Implement%20a%20stack%20using%20a%20linked%20list.ipynb)

- `push`
- `pop`
- `size`
- `is_empty`

---

## Advanced

### [Implement a stack using a deque](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/stack/Implement%20a%20stack%20using%20a%20deque.ipynb)

---

### [Implement a stack using a LifoQueue](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/stack/Implement%20a%20stack%20using%20a%20LifoQueue.ipynb)

---

### [Practice: Balanced Parentheses(Python List)](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/stack/Balanced%20Parentheses%20Exercise%20-%20Stacks.ipynb)

- `equation_checker`

---

### [Reverse Polish Notation(Linked List)](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/stack/Reverse%20Polish%20notation.ipynb)

**Reverse Polish notation**, also referred to as **Polish postfix notation** is a way of laying out operators and operands.

When making mathematical expressions, we typically put arithmetic operators (like `+`, `-`, `*`, and `/`) _between_ operands. For example: `5 + 7 - 3 * 8`

However, in Reverse Polish Notation, the operators come _after_ the operands. For example: `3 1 + 4 *`

The above expression would be evaluated as `(3 + 1) * 4 = 16`

The goal of this exercise is to create a function that does the following:

-   Given a _postfix_ expression as input, evaluate and return the correct final answer.

**Note**: In Python 3, the division operator `/` is used to perform float division. So for this problem, you should use `int()` after every division to convert the answer to an integer.

- `eval`: and safety issues

---

### [Reverse a Stack(Linked Lists)](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/stack/Reverse%20a%20stack.ipynb)

- `reverse_stack`

---

### [Minimum Bracket Reversals(Linked List)](https://github.com/ZacksAmber/Udacity-Data-Structure-Algorithms/blob/main/2/1-3/stack/Minimum%20bracket%20reversals.ipynb)

Given an input string consisting of only `{` and `}`, figure out the minimum number of reversals required to make the brackets balanced.

For example:

-   For `input_string = "}}}}`, the number of reversals required is `2`.

-   For `input_string = "}{}}`, the number of reversals required is `1`.

If the brackets cannot be balanced, return `-1` to indicate that it is not possible to balance them.
