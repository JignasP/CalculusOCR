#!/usr/bin/env python

from setuptools import setup,find_packages


from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / 'README.md').read_text(encoding='utf-8')


setup(
    name='CalculusOCR',
    version='0.0.1',
    description='CalculusOCR: Using a ViT to solve images of equations .',
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
    install_requires=['pillow','pix2tex'],
   
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',        
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
)