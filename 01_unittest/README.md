# My Project

This is a simple calculator project implemented in Python. It provides basic arithmetic operations as well as some scientific functions.

## Features

- Basic arithmetic operations: addition, subtraction

## Coding Style

### Project Structure

The project follows a flat layout for simplicity.

```
01_unittest/
├── calculator/
│ ├── __init__.py
│ └── arithmetic.py
├── tests/
│ ├── __init__.py
│ └── test_arithmetic.py
└── setup.py
```

## Usage

### Installation

Use `pip` to install the project:

```bash
pip install .
```

### Run Test

#### unittest

To run tests using unittest, you can use the following command:

```bash
python -m unittest
```

unittest supports these command-line options:

- `-b`, `--buffer`: Buffer stdout and stderr during tests
- `-c`, `--catch`: catch 住 error 或 failure 直到當前測試跑完
- `-f`, `--failfast`: 一旦出現 error 或 failure 就停止
- `--locals`: Show local variables in tracebacks
- `--durations` N: 顯示最慢的前 N 個 test cases (若 N=0 會顯示所有 test cases)

#### Using unittest discover

Run all tests with verbose output:

```bash
python -m unittest discover --verbose
```

Run a specific test file with verbose output:

```bash
python -m unittest discover -v -p test_arithmetic.py
```

The `discover` sub-command has several options:

- `-v`, `--verbose`: Verbose output
- `-s`, `--start-directory`: Directory to start discovery (`.` default)
- `-p`, `--pattern`: pattern to match test files (`test*.py` default)
- `-t`, `--top-level-directory`: Top level directory of project (defaults to start directory)

#### Run a Single Test File

To run a single test file directly:

```bash
python tests/test_arithmetic.py
```
