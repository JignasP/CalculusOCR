
from PIL import Image

from PIL import Image
from pix2tex.cli import LatexOCR
from sympy.parsing.latex import parse_latex

img = Image.open('C:/Users/Jignas/Downloads/eqn5.jpg')
model = LatexOCR()
print(model(img))
latex_string = model(img)
# {\frac{d f}{d t}}=\operatorname*{lim}_{h\to0}{\frac{f(t+h)-f(t)}{h}}
#latex_string = r" {\frac{d f}{d t}}=\operatorname*{lim}_{h\to0}{\frac{f(t+h)-f(t)}{h}}"

equation = parse_latex(latex_string)
print (equation)

# a=sp.Eq(Derivative(f, t), operatorname*(l*(i*m)))



