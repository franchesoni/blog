
# Python tooling

## **TL;DR**
how to convert a python project to a well-maintained python project using tools

## Motivation
I am building a framework for interactive image segmentation. However, other than organizing the code in folders and making imports from the base directory, the project has no sophistication (I use git, but it's only me).

I found myself modifying the README each time I wanted to register that something was changing. Not convenient. The things I'm looking for is some sort of:

- automatic formatting
- automatic code checking (no bugs)
- automatic documentation

in the future:

- automatic testing
- type checking
- package managing

## Resources
my sources:
- https://www.youtube.com/watch?v=q8DkatMZvUs&t=399s&ab_channel=anthonywritescode
- https://medium.com/georgian-impact-blog/python-tooling-makes-a-project-tick-181d567eea44
- my experience

## Dive in

### `pre-commit`

#### Explanation
Utility that will run some tools automatically at each commit. It can also be run whenever using `pre-commit run --all-files`.


#### Install
```
pip install pre-commit
```

#### Setup
```
pre-commit sample-config > .pre-commit-config.yaml
```
We will continue adding utilities. When we finish, we should run `pre-commit install` on the git dir.

### `pyupgrade` 

#### Explanation
Changes some expressions to the most modern way of writing them

#### Install
Append the following to `.pre-commit-config.yaml`
```
-   repo: https://github.com/asottile/pyupgrade
    rev: v2.31.1
    hooks:
    -   id: pyupgrade
```

### `isort`
#### Explanation
Automatically sorts imports
#### Install
Append the following to `.pre-commit-config.yaml`
```
-   repo: https://github.com/pycqa/isort
    rev: 5.10.1
    hooks:
      - id: isort
        name: isort (python)
```

### `black`

#### Explanation
Automatically formats code

#### Install
Append the following to `.pre-commit-config.yaml`
```
-   repo: https://github.com/psf/black
    rev: 22.1.0
    hooks:
      - id: black
        # It is recommended to specify the latest version of Python
        # supported by your project here, or alternatively use
        # pre-commit's default_language_version, see
        # https://pre-commit.com/#top_level-default_language_version
        language_version: python3.9
```
### `darglint`
#### Explanation
This is a documentation formatter and checker

#### Install
Append the following to `.pre-commit-config.yaml`
```
-   repo: https://github.com/terrencepreilly/darglint
    rev: master
    hooks:
    - id: darglint
```

### `flake8`
#### Explanation
Linter: will check the code for bugs.

#### Install
Append the following to `.pre-commit-config.yaml`
```
-   repo: https://github.com/pycqa/flake8
    rev: ''  # pick a git hash / tag to point to
    hooks:
    -   id: flake8
```

### `prospector`
#### Explanation
Prospector is a tool to analyse Python code and output information about errors, potential problems, convention violations and complexity.

#### Install
Append the following to `.pre-commit-config.yaml`
```
repos:
-   repo: https://github.com/PyCQA/prospector
    rev: 1.7.5
    hooks:
    -   id: prospector
        additional_dependencies:
        - ".[with_mypy,with_bandit]"
```

### Now go back to `pre-commit` and finish the install

--- 
### `sphinx`

#### Explanation
Automatic documentation from code

#### Install
This is more tricky than the previous ones.  

install

```pip install sphinx```

answer the questions to generate docs structure

```sphinx-quickstart docs```

on the file `docs/source/conf.py` fill the extensions list as follows:
```python
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
]
```

I have my code organized close to the [recommendation](https://packaging.python.org/en/latest/tutorials/packaging-projects/):
```
project/
├── LICENSE  # I don't have this
├── pyproject.toml  # I don't have this
├── README.md  # mine is `.rst`
├── setup.cfg
├── src/  # different contents
│   └── example_package/
│       ├── __init__.py
│       └── example.py
└── tests/
```

with a `setup.cfg` containing
```
[metadata]
name = example-package-YOUR-USERNAME-HERE
version = 0.0.1
author = Example Author
author_email = author@example.com
description = A small example package
long_description = file: README.md
long_description_content_type = text/markdown
url = https://github.com/pypa/sampleproject
project_urls =
    Bug Tracker = https://github.com/pypa/sampleproject/issues
classifiers =
    Programming Language :: Python :: 3
    License :: OSI Approved :: MIT License
    Operating System :: OS Independent

[options]
package_dir =
    = src
packages = find:
python_requires = >=3.6

[options.packages.find]
where = src
```

then we can do

`python -m pip install -e .`



### Read the docs

#### Explanation
Free documentation hosting.

#### Install
You'll have to create a user following the first parts of [this tutorial](https://docs.readthedocs.io/en/stable/tutorial/). 


### Other
- look for mot pre-commit hooks here: https://pre-commit.com/hooks.html


## Notes
- run `pre-commit autoupdate` from time to time to update the hooks.

## Other tools
### `pydantic`

#### Explanation
Type checker. I won't add it now (my code is not prepared).



