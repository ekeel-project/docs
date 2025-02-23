# EKEEL Documentation

Welcome to the EKEEL documentation repository. This repository uses [MkDocs](https://www.mkdocs.org/) to generate and host the documentation for the EKEEL project.

## Overview

EKEEL (Empowering Knowledge Extraction to Empower Learners) is a project aimed at providing tools and services for knowledge extraction and transcription. This repository contains the documentation for the EKEEL project, including setup guides, deployment instructions, and code references.

## Repositories

The EKEEL project consists of two repositories:

- [Annotator](https://github.com/ekeel-project/annotator): This repository contains the code for the annotator service.
- [Augmentator](https://github.com/ekeel-project/augmentator): This repository contains the code for the augmentator service.

## Documentation

The documentation is organized using MkDocs with the Material theme. The documentation includes:

- **Quickstart Guides**: Instructions to quickly set up and deploy the services.
- **Codebase Documentation**: Detailed documentation of the codebase, generated using mkdocstrings.
- **Deployment Guides**: Step-by-step guides to deploy the services locally and remotely.

## Getting Started

To build and serve the documentation locally, follow these steps:

1. Clone this repository:
    ```bash
    git clone https://github.com/ekeel-project/ekeel.git
    cd ekeel
    ```

2. Clone `annotator` and `augmentator` repositories:
    ```bash
    mkdir -p apps
    git clone https://github.com/ekeel-project/annotator.git apps/annotator
    git clone https://github.com/ekeel-project/annotator.git apps/augmentator
    ```

3. Install the required dependencies:
    ```bash
    pip install -r mkdocs/requirements.txt
    ```

4. Build and serve the documentation:
    ```bash
    mkdocs serve
    ```

5. Open your browser and navigate to `http://127.0.0.1:8000` to view the documentation.

## Contributing

We welcome contributions to improve the documentation. If you find any issues or have suggestions, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
