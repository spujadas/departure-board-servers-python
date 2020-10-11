"""
Setup for departure server with pygame backend module
"""

from setuptools import setup, find_namespace_packages

with open("../README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="departure-server-pygame",
    version="1.0.0",
    author="Sébastien Pujadas",
    author_email="sebastien@pujadas.net",
    description="Pygame Departure board back end",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/spujadas/departure-board-servers-python",
    packages=find_namespace_packages(include=["departure.renderer.*"]),
    install_requires=[
        "departure",
        "pygame",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
