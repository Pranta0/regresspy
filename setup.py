from setuptools import setup
from setuptools import find_namespace_packages

# Load the README file.
with open(file="README.md", mode="r") as readme_handle:
    long_description = readme_handle.read()

setup(
    name='regresspy',

    # Define the author of the repository.
    author='Paul Pranta',

    # Define the Author's email
    author_email='prantapaul727@gmail.com',

    # Define the version of this library.
    version='0.1.0',

    description='regresspy is a python module for carrying out simple regressions using gradient descent algorithm',

    long_description=long_description,

    # Here is the URL where you can find the code, in this case on GitHub.
    url='https://github.com/Paul Pranta/regresspy/tree/Paul Pranta',
    # Here are the keywords of my library.
    keywords='gradient descent algorithm, regression, loss',

    # here are the packages I want "build."
    packages=find_namespace_packages(include=['regresspy', 'regresspy.*']),

    # These are the dependencies the library needs in order to run.
    install_requires=[
        'conda==4.10.1',
        'numpy==1.19.5',
        'scikit-image==0.18.1',
        'scikit-learn',
    ]
)