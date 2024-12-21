from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    Reads dependencies from a requirements.txt file and returns them as a list.
    Removes '-e .' if present, as it is specific to editable installations.
    """
    requirements = []
    with open(file_path, "r") as file:
        # Read all lines and strip whitespace
        lines = file.readlines()
        requirements = [line.strip() for line in lines if line.strip()]
        
        # Remove '-e .' if it exists
        if "-e ." in requirements:
            requirements.remove("-e .")
    
    return requirements

setup(
    name="Cardiovascular Risk Prediction",
    version="0.0.1",
    author="Abhijeet Kumar",
    author_email="abhijeet.kr7252@gmail.com",
    description="ML model to predict cardiovascular risk",
    url="https://github.com/abhikr11/Cardio_Risk_Pred",
    packages=find_packages(),  # Automatically finds all sub-packages
    install_requires=get_requirements("requirements.txt")  # Reads requirements from file
)