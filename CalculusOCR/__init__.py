import subprocess
subprocess.call(['pip', 'install', 'antlr4-python3-runtime==4.11.0'])
subprocess.call(['pip', 'install', 'pix2tex==0.1.2'])

from .CalculusOCR import solveimage ,sympy_solve
