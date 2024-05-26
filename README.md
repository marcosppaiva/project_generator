# Project Generator

## Description

**Project Generator** is a Python package that creates a folder and file structure for new data science or data engineering projects. It helps standardize project organization, saving time and ensuring consistency.

## Structure Created

O comando cria a seguinte estrutura de diretórios e arquivos:

```
Root
├── src/                   # Source code of the project.
├── README.md              # Project overview and documentation.   
├── requirements.txt       # List of project dependencies.
├── pyproject.toml         # Project configuration and metadata.
├── .env                   # File stores environment-specific variables that can be loaded into your application.
├── data/                  # Directory for data files.
│ ├── processed/           # Processed data ready for use.
│ └── raw/                 # Raw, unprocessed data.
├── docs/                  # Documentation files.
└── notebooks/             # Jupyter notebooks for data analysis and experimentation.
```

## Instalation

To install ** Project Generator**, follow the steps below:

1. Clone the repository or download the project files.
2. In the terminal navigate to the directory containing the `pyproject.toml` file.
3. Run the installation command:

    ```sh
    pip install .
    ```

## Usage

After installation, you can use the project-generate command to create the folder structure. 
For example
```ssh
project-generate /path/to/your/project
```

## Contribution

Contributions are welcome! Feel free to open issues or pull requests. Please follow best coding practices and ensure all tests are passing before submitting a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.