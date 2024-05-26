from setuptools import find_packages,setup
def get_requirements(file_path):
    with open(file_path) as f:
        requirements = f.read().splitlines()
         
        requirements.pop()
        # print(requirements)
setup(
    name="mlproject",
    version="0.0.1",
    author="Jayadir",
    author_email="jayadir102005@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)