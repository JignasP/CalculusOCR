
from PIL import Image
from pix2tex.cli import LatexOCR
from sympy.parsing.latex import parse_latex
from sympy import *
import sympy
import re

def ocr(url):
    img = Image.open(url)
    model = LatexOCR()
    latex_string = model(img)
    equation = parse_latex(latex_string)
    print(equation)
    return equation

def solve(eqn):
    
    words = re.findall(r'\b[A-Za-z]+\b', str(eqn))
    list = []
    for word in words:
        if word not in dir(sympy) and word not in list:
           list.append(word)

    symb = symbols(" ".join(list))
    ans = eqn.doit()
    print("After Integration : {}".format(ans))
    return ans

if __name__ == '__main__':

    url = '/image.png'
    eqn = ocr(url)
    ans = solve(eqn)

