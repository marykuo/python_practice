# 02_pytest

This is a simple calculator project implemented in Python. It provides basic arithmetic operations as well as some scientific functions.

## Features

- Basic arithmetic operations: addition, subtraction

## Coding Style

### Project Structure

The project follows a flat layout for simplicity.

```
02_pytest/
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

[Pytest 官方文件](https://pytest.org)

#### pytest

```bash
pytest -vv
```

### 計算 Coverage

- add dependency `pytest-cov`
