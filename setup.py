from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        [req.replace('\n', '') for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        return requirements

setup(
    name='Diamond_Price_Predction',
    version='0.0.1',
    author='Sri Darsan Sah',
    author_email='sridarsansah5907@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)