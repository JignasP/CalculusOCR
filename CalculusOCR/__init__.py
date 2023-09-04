import subprocess
import importlib
import subprocess


requirements_file=['pix2tex','antlr4-python3-runtime==4.11.0','sympy']
def install_package(package_name):
    try:
        importlib.import_module(package_name)
    except ImportError:
        subprocess.check_call(["pip", "install", package_name])

for package in requirements_file:
    install_package(package)

from .CalculusOCR import solveimage, sympy_solve, getlatex
