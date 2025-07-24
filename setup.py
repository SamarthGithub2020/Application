"""
The setup.py file is an essential part of packaging and distributing python projects. Its used by setuptools to define the
configuration of your project, such as its metadata,dependencies, etc    
"""

from setuptools import find_packages, setup  ##the find_packages scans all the folders and in whichever folders it finds the __init__.py, it considers those as a package
from typing import List

def get_requirements()->List[str]:
    """
This function returns the list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open("requirements.txt",mode="r") as file:
            #Read lines from the file
            lines=file.readlines()
        #Processing each line
            for line in lines:
                requirement=line.strip() #.stip() function cuts off the unnecessary spaces present between the lines/paragraphs
                #Ignoring the empty line and -e .
                if requirement and requirement!= "-e .":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Samarth Vaishnav",
    packages=find_packages(),
    install_requires=get_requirements()
)



