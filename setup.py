from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns the verified list of requirement strings.
    '''
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='Credit_card_fraud_detection',
    version='0.0.1',
    author='Shiham',
    author_email='shihamfm@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)