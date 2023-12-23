from setuptools import setup, find_packages

setup(
    name='qunet',
    packages=find_packages(include=['qunet']),
    version='0.1.0',
    description='Quantum Network Descriptor Language',
    author='Alejandro Gonzalvo',
    install_requires=['networkx==3.2.1', 'matplotlib==3.8.2'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.4.3'],
    test_suite='tests',
)