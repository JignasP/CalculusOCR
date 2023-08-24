
from PIL import Image
from pix2tex.cli import LatexOCR
from sympy.parsing.latex import parse_latex
from sympy import *

def ocr(url):
    img = Image.open(url)
    model = LatexOCR()
    latex_string = model(img)
    equation = parse_latex(latex_string)
    print(equation)
    return equation

def solve(eqn):

    x, y = symbols('x y')
    #eqn = Integral(sqrt(y ** 2 + 1), y)
    ans = eqn.doit()
    print("After Integration : {}".format(ans))
    return ans

if __name__ == '__main__':

    url = '/eqn.png'
    eqn = ocr(url)
    ans = solve(eqn)

