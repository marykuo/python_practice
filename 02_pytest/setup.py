from setuptools import setup, find_packages

setup(
    name="02_pytest",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    setup_requires=[
        "pytest-runner",
    ],
    tests_require=[
        "pytest",
    ],
    entry_points={
        "console_scripts": [],
    },
)
