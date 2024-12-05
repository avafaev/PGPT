import os
from collections import OrderedDict
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "requirements.txt")) as f:
    dependencies = f.read().strip().split("\n")

setup(
    name="sspentestlab",
    version="0.13.3",
    description="SSPentestLab, a GPT-empowered penetration testing tool",
    long_description="""
    SSPentestLab is a penetration testing tool empowered by ChatGPT.
    It is designed to automate the penetration testing process. It
    is prototyped initially on top of ChatGPT and operate in an
    interactive mode to guide penetration testers in both overall
    progress and specific operations.
    """,
    author="Ali Vafaev, Tomás Bastante",
    author_email="ali.vafaev@soprasteria.com, tomas.bastante@soprasteria.com",
    maintainer="Ali Vafaev, Tomás Bastante",
    maintainer_email="ali.vafaev@soprasteria.com, tomas.bastante@soprasteria.com",
    url="https://github.com/TomasBastanteFlor/PGPT",
    project_urls=OrderedDict(
        (
            ("Code", "https://github.com/TomasBastanteFlor/PGPT"),
            ("Issue tracker", "https://github.com/TomasBastanteFlor/PGPT"),
        )
    ),
    license="MIT License",
    packages=["sspentestlab"] + find_packages(),
    # packages=find_packages(),
    # scripts=['sspentestlab/main.py'],
    install_requires=dependencies,
    entry_points={
        "console_scripts": [
            "sspentestlab=sspentestlab.main:main",
            "sspentestlab-cookie=sspentestlab.extract_cookie:main",
            "sspentestlab-connection=sspentestlab.test_connection:main",
        ]
    },
)
