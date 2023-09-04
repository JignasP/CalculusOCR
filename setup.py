#!/usr/bin/env python

from setuptools import setup, find_packages
from pathlib import Path
import subprocess
import os
subprocess.run(['pip', 'install', 'pbr'])
import pbr.version

version_info = pbr.version.VersionInfo('CalculusOCR')


this_directory = Path(__file__).parent
long_description = (this_directory / 'README.md').read_text(encoding='utf-8')


setup(
    name='CalculusOCR',
    version= version_info.release_string(),
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
        'Development Status :: 4 - Beta ',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Text Processing :: Markup :: LaTeX',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
)
