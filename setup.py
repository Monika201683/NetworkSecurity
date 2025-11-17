"""
The setup.py file essential part of the packaging and distribution process for python projects.
it is uused by setuptools  to define the configuration of the projects,
as well as its dependencies, metadata.
"""

from setuptools import setup, find_packages
from typing import List


def get_requirements() -> List[str]:
    """This function will return list of requirements."""
    requirements_lst: List[str] = []
    try:
        with open("requirements.txt", "r") as file:
            lines = file.readlines()

            for line in lines:
                requirements = line.strip()
                if requirements and requirements != "-e .":
                    requirements_lst.append(requirements)
    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirements_lst


print(get_requirements())
setup(
    name="NetworkSecurity",
    version="0.1.0",
    author="Krish",
    author_email="krish@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
    description="A package for network security analysis.",
)
