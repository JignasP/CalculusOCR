# CalculusOCR


## Introduction

[CalculusOCR](https://github.com/JignasP/CalculusOCR) is a Python package designed to simplify the process of converting handwritten calculus expressions into LaTeX code, converts then into Sympy equation and solving them. 

### Key Features

1. **OCR-Powered Input:** Easily convert images containing handwritten calculus expressions into a digital format.

2. **SymPy Integration:** Utilize SymPy's mathematical capabilities to perform calculations on LaTeX code generated from handwritten expressions.

3. **Versatile Problem Handling:** Solve a wide range of calculus problems, including derivatives, integrals, limits, and complex mathematical expressions.

## Applications:
   - **Educational Materials:** Create assignments, quizzes, tests, or exams with handwritten calculus problems.
   - **Research and Reporting:** Incorporate complex calculus equations and formulas into research papers, reports, or presentations.
   - **Problem Solving:** Solve challenging calculus problems using Python .
   - **Teaching and Learning:** Enhance calculus education through interactive notebooks or online platforms.

## License

CalculusOCR is licensed under the MIT License.The full text of the MIT License in the [LICENSE](https://github.com/JignasP/CalculusOCR/blob/main/LICENSE) file.

## Installation

To install CalculusOCR using pip:

```bash
pip install CalculusOCR
```


### Importing the Package

```python
from CalculusOCR import *
```

### OCR-Powered Conversion

Convert a handwritten calculus expression image into LaTeX code:

```python
LaTeX = getlatex("<handwritten_expression.jpg>")
```

### Solving Sympy Equation

Use SymPy to perform mathematical operations:

```python
solution = sympy_solve(<SympyEquation>)
```
### Solving Calculus Problems

Use solveimage() to perform mathematical operations in the given image:

```python
SympyEqn, solution = solveimage("<calculus_expression.jpg>")
```


## Contributing
Whether you have ideas, translations, design changes, code cleaning, or even major code changes, help is always welcome. The app gets better and better with each contribution, no matter how big or small! If you'd like to get involved, check our [contribution notes](CONTRIBUTING.md).

Please note that all participants in this project are expected to follow our Code of Conduct. By participating in this project you agree to abide by its terms. See [CODE\_OF\_CONDUCT.md](CODE_OF_CONDUCT.md).

