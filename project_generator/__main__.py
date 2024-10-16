import os
import argparse

_DIRS = ['src', 'data', 'data', 'data/raw', 'data/processed', 'docs', 'notebooks']

_FILES = ['README.md', 'requirements.txt', 'pyproject.toml', '.env']

_PYPROJECT_TEMPLATE = '''
[tool.pylint.messages_control]
disable = [
    "missing-function-docstring",
    "missing-final-newline",
    "missing-class-docstring",
    "missing-module-docstring",
    "invalid-name",
    "too-few-public-methods",
    "anomalous-backslash-in-string",
    "f-string-without-interpolation",
    "logging-fstring-interpolation",
    "import-error",
    "ungrouped-imports",
    "no-name-in-module",
    "too-many-arguments",
    "global-statement"
]

[tool.pylint.MASTER]
init-hook='import sys; sys.path.append(".")'

[tool.black]
line-length = 88
target-version = ['{python_version}']
skip-string-normalization = true

[tool.isort]
multi_line_output = 3
length_sort = true
'''


def get_python_version():
    while True:
        version = input('Python version used? (e.g: ^3.9): ')
        return version


def create_project_structure(root_path: str, python_version: str) -> None:

    for directory in _DIRS:
        dir_path = os.path.join(root_path, directory)
        os.makedirs(dir_path, exist_ok=True)
        print(f'Created directory: {dir_path}')

    for file in _FILES:
        file_path = os.path.join(root_path, file)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('')
        print(f'Created file: {file_path}')

    pyproject_content = _PYPROJECT_TEMPLATE.format(python_version=python_version)
    pyproject_path = os.path.join(root_path, 'pyproject.toml')
    with open(pyproject_path, 'w', encoding='utf-8') as f_in:
        f_in.write(pyproject_content)
    print(f'Created file: {pyproject_path} with customized content')


def main() -> None:

    parse = argparse.ArgumentParser(description='Create project structure')
    parse.add_argument('root', type=str, help='Root directory of the project')
    args = parse.parse_args()

    python_version = get_python_version()
    create_project_structure(args.root, python_version)


if __name__ == '__main__':
    main()
