![PyPI - License](https://img.shields.io/pypi/l/pytmlib)
![GitHub tag (with filter)](https://img.shields.io/github/v/tag/ofabel/pytm-example)
![GitHub issues](https://img.shields.io/github/issues/ofabel/pytm-example)

# pytm-example

This repository contains various example exercises for the _Python Tool Manager_.
You can find more information on the _Python Tool Manager_ in the
corresponding [documentation on GitHub](https://ofabel.github.io/pytm-bootstrap/).

## Requirements

* [Python](https://www.python.org/) version 3.8 or higher.
* Access to the Python Tool Manager.
* [Pycharm CE or Professional](https://www.jetbrains.com/pycharm/) (not mandatory, but recommended).
* Basic knowledge of the Python programming language.
* Basic knowledge on how to use a terminal window.

## Quickstart

Proceed the following steps to set up your project:

1. [Clone](#clone-this-repository) or [download](https://github.com/ofabel/pytm-example/archive/refs/heads/master.zip)
   this repository.
2. [Create a virtual Python environment](#create-a-virtual-python-environment).
3. Activate the virtual environment and [install the dependencies](#install-the-dependencies).
4. [Run some exercises](#run-an-exercise).

### Clone this Repository

Open a new terminal window, navigate to your desired folder on your local hard disk and execute the following command:

```shell
git clone git@github.com:ofabel/pytm-example.git
```

### Create a Virtual Python Environment

Open a terminal window, navigate to the cloned or downloaded repository folder and execute the following command:

```shell
python -m venv venv
```

This will create a new `venv` folder, containing the virtual environment. It's mandatory, that folder's name is `venv`.

### Install the Dependencies

Open a terminal window, navigate to the cloned or downloaded repository
folder, [activate the virtual environment](https://docs.python.org/3/library/venv.html#how-venvs-work) and execute the
following command:

```shell
pip install -r requirements.txt
```

### Run an Exercise

To run an exercise you need to open a terminal window, navigate to the cloned or downloaded repository folder and
activate the virtual environment. Now, navigate to the desired exercise folder and execute the following command:

```shell
flask run --debug
```

### The Whole Procedure

The following listing shows the whole procedure for a bash-compatible terminal:

```shell
# clone the repository
git clone git@github.com:ofabel/pytm-example.git

# change the current working directory to the just created folder
cd pytm-example

# create the virtual environment
python -m venv venv

# activate the just created virtual environment
source venv/bin/activate

# install the dependencies
pip install -r requirements.txt

# change to a exercise folder and run the exercise
cd plot
flask run --debug
```
