# Power Method
A Python implementation of the Power Method (Power Iteration) to approximate the dominant eigenvalue and its corresponding eigenvector of a n×n square matrix.

#  Overview
In this project, I implemented the method using basic Python operations without relying on external numerical libraries.

# Features
- Supports square matrices of arbitrary n×n order.
- Performs matrix-vector multiplication.
- Iteratively approximates the dominant eigenvalue and corresponding eigenvector.
- Accepts user-defined matrices and initial vectors.
- Uses a convergence condition to determine when to stop the iteration.

# Requirements
- Python 3.x
- No external libraries required.

# Input Requirements
1. The matrix must be square.
2. All matrix entries must be integers.
3. The initial vector must have the same order as the matrix.
4. The initial Eigen vector must contain exactly one element equal to `1`, while all other elements must be `0`.

Example:

```python
A = [
    [4, 2],
    [1, 3]
]

V = [0, 1]
```

# How to Run
1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the Python file:
  ```bash
  python power_method.py
  ```
4. Enter the matrix order, matrix elements row by row, and the initial vector when prompted.

# Limitations
- The initial Eigen vector(V) must follow the specified format.
- The current implementation uses integer matrix inputs.

# Learning Objectives
This project was developed to practice:

- Numerical methods and iterative algorithms.
- Matrix-vector multiplication.
- Eigenvalue and eigenvector computation.
- Python loops, lists, conditional statements, and input validation.

# Author

Developed as a personal Python project while exploring numerical methods and scientific computing.
