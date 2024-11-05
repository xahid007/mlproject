from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-.e"
def get_requirements(file_path:str)->List[str]:

    '''
    This function will install the requirements List


    '''

    requirements = []
    with open(file_path) as file_obj:
        requiremennts = file_obj.readlines()
        requiremennts = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requiremennts:
            requiremennts.remove(HYPEN_E_DOT)
    
    return requiremennts



setup(
    name='mlproject',
    version='0.0.1',
    author='Zahid Hasan',
    author_email='zhasan708@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)