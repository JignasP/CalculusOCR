from PIL import Image
from pix2tex.cli import LatexOCR
from sympy.parsing.latex import parse_latex
from sympy import *
import sympy
import re
import argparse


def sympy_solve(sympy_equation):
    words = re.findall(r'\b[A-Za-z]+\b', str(sympy_equation))

    var_list = []
    for word in words:
        if word not in dir(sympy) and word not in var_list:
            var_list.append(word)

    sympy_symbols = symbols(" ".join(var_list))

    solution = sympy_equation.doit()

    return solution


def solve(file):
    img = Image.open(file)
    model = LatexOCR()
    latex_string = model(img)
    equation = parse_latex(latex_string)
    return equation, sympy_solve(equation)


if __name__ == '__main__':
    descStr = "CalculusOCR"
    parser = argparse.ArgumentParser(description=descStr)
    parser.add_argument('--file', dest='filename', required=True)
    filename = parser.parse_args().filename

    eqn, sol = solve(filename)
    print("Equation : ", eqn)
    print("Solution : {}".format(sol))
