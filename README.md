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

### Mac OSX

Due to the System Integrity Protection (SIP, https://en.wikipedia.org/wiki/System_Integrity_Protection) it is
not allowed to have relative paths for linked shared libraries. To avoid the protection by the system please replace
the relative path with an absolute path to the libdeeply.dylib:

```
cd ~/deeply-python-demo

install_name_tool -change libdeeply.dylib $PWD/lib/libdeeply.dylib lib/_deeply.so
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
