from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirement= []
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace('\n',"") for req in requirement]
    return requirement

setup(
name='mlproject',
version='0.0.1',
author= 'aish',
author_email='aakkim@asu.edu',
packages=find_packages(),
install_requires=get_requirements('requirement.txt')
)