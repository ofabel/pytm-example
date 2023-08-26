# pytm-example

This repository contains various example exercises for the _Python Tool Manager_.

## Requirements

* Python >= 3.9
* Access to the Python Tool Manager
* Pycharm CE or Professional (not mandatory, but recommended)
* Basic knowledge in the Python programming language

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
following commands:

```shell
pip install -r requirements.txt
pip install -r requirements-test.txt
```

### Run an Exercise

To run an exercise you need to open a terminal window, navigate to the cloned or downloaded repository folder and
activate the virtual environment. Now, navigate to the desired exercise folder and execute the following command:

```shell
flask run --debug
```
