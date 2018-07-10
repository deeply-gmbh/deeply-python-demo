# Deeply Pyhton Demo

This simple demo project shows how to use deeply with our Python wrapper in a Python application. 

See the straight-forward usage in less then 20 lines of code in Main.py and ContentListener.py.

## Project setup

### deeply SDK

First things first. After cloning this repo to your home dir (~/) you need to copy your deeply shared library,
the pyhon wrapper shared library and the deeply.py to the lib directory:

```
cp ~/deeply-python-{VERSION}/*deeply* ~/deeply-python-demo/lib
```

You also need to copy your license.txt (assuming stored in your home dir) to the project root dir.

```
cp ~/license.txt ~/deeply-python-demo
```

## Run

### Main.py

#### With JetBrains PyCharm

Open the project with PyCharm and run the Main.py

#### From command line

Or directly run it with from your command line

```
cd ~/deeply-java-demo/

python Main.py
```

### Unit Tests

#### Dependency: PyHamcrest

We use assert_that statements from PyHamcrest for better readability. Please have look here 
https://github.com/hamcrest/PyHamcrest . 

#### With JetBrains PyCharm

Open the project with PyCharm and run the unit tests in the test dir by right-clicking on "test" and choosing 
"Run 'Unittests in test'".

#### From command line

```
cd ~/deeply-java-demo/

python -m unittest discover -s ./test -t .
```
