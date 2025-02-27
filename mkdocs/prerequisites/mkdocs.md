# Mkdocs
-------

The EKEEL project is documented with [mkdocs](https://www.mkdocs.org/getting-started/)

Its update is fully automated with every code modification, as long as classes and functions are documented in the [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html) format.

To modify and view the live-updated content locally:

1. Clone the repos inside `apps` folder
```bash
mkdir apps
cd apps
git clone https://github.com/ekeel-project/annotator.git
git clone https://github.com/ekeel-project/augmentator.git
```

2. Install the packages from the ```requirements.txt``` file located in the ```mkdocs``` directory in a new environment:
```bash
pip install -r mkdocs/requirements.txt
mkdocs serve
``` 

3. Open your browser and navigate to `http://127.0.0.1:8000/docs/` to view the documentation.

!!! warning
    Use a different environment from ```ekeel_anno_env``` and ```ekeel_aug_env``` (the two environments of the project) to avoid mixing packages and create possible conflicts