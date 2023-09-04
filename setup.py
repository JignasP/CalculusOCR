#!/usr/bin/env python

from setuptools import setup, find_packages
from pathlib import Path
import subprocess
import os

cocr_remote_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

print(cocr_remote_version)

with open('CalculusOCR/version.txt', "w") as file:
    file.write(cocr_remote_version)
    print("Done")

'''
if "-" in cocr_remote_version:

    v,i,s = cocr_remote_version.split("-")
    cocr_remote_version = v + "+" + i + ".git." + s

print("2",cocr_remote_version)

assert os.path.isfile("CalculusOCR/version.py")

with open("CalculusOCR/VERSION", "w", encoding="utf-8") as fh:
    fh.write("%s\n" % cocr_remote_version)
'''

this_directory = Path(__file__).parent
long_description = (this_directory / 'README.md').read_text(encoding='utf-8')

with open('CalculusOCR/version.txt', "r") as file:
    version_no = file.read()

setup(
    name='CalculusOCR',
    version= version_no,
    description=' CalculusOCR: A Vision Transformer that can perform optical character recognition on handwritten calculus expressions and outputs LaTeX code, Sympy equation and solution.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Jignas Paturu',
    author_email='jignas.paturu@hotmail.com',
    url='https://github.com/JignasP/CalculusOCR/',
    license='MIT',
    keywords=[
        'artificial intelligence',
        'image to text',
        'calculus'
    ],
    packages=find_packages(),
    install_requires=[],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Text Processing :: Markup :: LaTeX',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
)
