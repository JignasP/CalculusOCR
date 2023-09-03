import subprocess

import subprocess, os


def check_and_install(package, version=None):
    result = subprocess.run(['pip', 'show', package], stdout=subprocess.PIPE, text=True)
    found = version is None or version in result.stdout
    if not found:
        subprocess.call(['pip', 'install', f'{package}' + (f'=={version}' if version else '')])
    return found


with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    for line in f:
        name, version = map(str.strip, line.split('==', 1))
        check_and_install(name, version if version else None)

from .CalculusOCR import solveimage, sympy_solve
