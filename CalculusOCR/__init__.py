import subprocess


def check_and_install(package, version=None):
    result = subprocess.run(['pip', 'show', package], stdout=subprocess.PIPE, text=True)
    found = version is None or version in result.stdout
    if not found:
        subprocess.call(['pip', 'install', f'{package}' + (f'=={version}' if version else '')])
    return found


with open('requirements.txt', 'r') as requirements_file:
    for line in requirements_file:
        package_info = line.strip().split('==')
        if len(package_info) >= 1:
            package_name = package_info[0]
            package_version = package_info[1] if len(package_info) == 2 else None
            check_and_install(package_name, package_version)

from .CalculusOCR import solveimage, sympy_solve, getlatex
