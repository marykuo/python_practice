from setuptools import setup, find_packages

setup(
    name="01_unittest",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # dependencies required for installing and using the package
    ],
    setup_requires=[
        # setup dependency
    ],
    tests_require=[
        # test dependency
        # test coverage dependency
    ],
    entry_points={
        "console_scripts": [
            # command-line scripts
        ],
    },
)
