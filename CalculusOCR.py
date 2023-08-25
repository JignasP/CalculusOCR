
from PIL import Image
from pix2tex.cli import LatexOCR
from sympy.parsing.latex import parse_latex
from sympy import *
import sympy
import re
import argparse

def ocr(file):
    img = Image.open(file)
    model = LatexOCR()
    latex_string = model(img)
    equation = parse_latex(latex_string)
    print("Equation : ",equation)
    return equation

def solve(eqn):


    words = re.findall(r'\b[A-Za-z]+\b', str(eqn))

    list = []
    for word in words:
        if word not in dir(sympy) and word not in list:
           list.append(word)

    symb = symbols(" ".join(list))


    ans = eqn.doit()
    print("Solution : {}".format(ans))
    return ans

if __name__ == '__main__':

    descStr = "CalculusOCR"
    parser = argparse.ArgumentParser(description=descStr)
    parser.add_argument('--file', dest='filename', required=True)
    filename = parser.parse_args().filename
    eqn = ocr(filename)
    ans = solve(eqn)

