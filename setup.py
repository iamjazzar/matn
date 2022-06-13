#!/usr/bin/env python
import re
from pathlib import Path

from setuptools import setup

this_directory = Path(__file__).parent
readme_text = (this_directory / "README.md").read_text()
long_description = re.sub(
    r"(\s*<picture>\s*|\s*</picture>\s*|\s*<source .* />\s*)", "", readme_text
)

setup(
    name="matn",
    version="0.2.2",
    packages=["matn"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "matn = matn.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development",
    ],
    url="https://github.com/iamjazzar/matn",
    license="MIT License",
    author="Ahmed Jazzar",
    author_email="me@ahmedjazzar.com",
    description="Arabic text processor tool.",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
