"""
Project home:
https://gitlab.com/szuro/pylarization
"""

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), 'r') as f:
    long_description = f.read()


setup(
    name='pylarization',
    version='0.1.8',
    description='Package for polarization state calculations',
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url='https://gitlab.com/szuro/pylarization',
    author='Robert Szulist',
    author_email='r.szulist@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    keywords='polarization light ellipse jones stokes mueller coherency',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['numpy'],
    test_suite="tests"
)
