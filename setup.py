from setuptools import find_packages, setup
setup(
    name='another-talib',
    packages=find_packages(include=['another_talib']),
    version='0.1.0',
    description='Another technical analysis library',
    author='Mariano Billinghurst',
    license='MIT',
    install_requires=['pandas'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)