import os

_DIRS = ['src', 'data', 'data', 'data/raw', 'data/processed', 'docs', 'notebooks']

_FILES = ['README.md', 'requirements.txt', 'pyproject.toml', '.env']


def create_project_structure(root_path: str) -> None:

    for directory in _DIRS:
        dir_path = os.path.join(root_path, directory)
        os.makedirs(dir_path, exist_ok=True)
        print(f'Created directory: {dir_path}')

    for file in _FILES:
        file_path = os.path.join(root_path, file)
        with open(file_path, 'w') as f:
            f.write('')
        print(f'Created file: {file_path}')


def main() -> None:
    import argparse

    parse = argparse.ArgumentParser(description='Create project structure')
    parse.add_argument('root', type=str, help='Root directory of the project')
    args = parse.parse_args()

    create_project_structure(args.root)


if __name__ == '__main__':
    main()
