from setuptools import setup, find_packages

setup(
    name='cvplot',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'plotly',
        # Add any other dependencies here
    ],
)
