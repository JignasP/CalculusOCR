
import subprocess
subprocess.call(['pip', 'install', 'Pillow>=10.0.0'])

from sympy import *
def sympy_solve(sympy_equation):
    import re
    import sympy

    words = re.findall(r'\b[A-Za-z]+\b', str(sympy_equation))

    var_list = []
    for word in words:
        if word not in dir(sympy) and word not in var_list:
            var_list.append(word)

    sympy_symbols = symbols(" ".join(var_list))

    solution = sympy_equation.doit()

    return solution


def solveimage(file):
    from PIL import Image
    from pix2tex.cli import LatexOCR
    from sympy.parsing.latex import parse_latex

    img = Image.open(file)
    model = LatexOCR()
    latex_string = model(img)
    equation = parse_latex(latex_string)
    return equation, sympy_solve(equation)


def main():
    import argparse

    desc_str = "CalculusOCR"
    parser = argparse.ArgumentParser(description=desc_str)
    parser.add_argument('--file', dest='filename', required=True)
    filename = parser.parse_args().filename

    eqn, sol = solveimage(filename)
    print("Equation : ", eqn)
    print("Solution : {}".format(sol))


if __name__ == '__main__':

    main()
