# My Project

This is a simple calculator project implemented in Python. It provides basic arithmetic operations as well as some scientific functions.

## Features

- Basic arithmetic operations: addition, subtraction

---
# Coding Style

## Project Structure

- flat layout

---
# Usage

## Installation

use `pip` to install it:

```bash
pip install .
```

## Run Test

```bash
python -m unittest
```

unittest supports these command-line options:
- `-b`, `--buffer`: ?
- `-c`, `--catch`: catch 住 error 或 failure 直到當前測試跑完
- `-f`, `--failfast`: 一旦出現 error 或 failure 就停止
- `--locals`: Show local variables in tracebacks
- `--durations` N: 顯示最慢的前 N 個 test cases (若 N=0 會顯示所有 test cases)

```bash
python -m unittest discover --verbose
python -m unittest discover -v -p test_arithmetic.py
```

discover sub-command:
- `-v`, `--verbose`: Verbose output
- `-s`, `--start-directory`: Directory to start discovery (`.` default)
- `-p`, `--pattern`: pattern to match test files (`test*.py` default)
- `-t`, `--top-level-directory`: Top level directory of project (defaults to start directory)
