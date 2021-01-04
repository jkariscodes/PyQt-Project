# PyQt Project
This is a PyQt project that has the aim of helping developers learn and appreciate desktop user interface design and 
implementation.

## About PyQt
PyQt is a graphical user interface (GUI) library developed by 
[RiverBank Computing Ltd](https://www.riverbankcomputing.com/) used to develop graphical user interfaces.
PyQt provides Python bindings for the Qt framework that is natively in C++ and provides bindings for Qt4 and Qt5 
versions.
PyQt5, which has been used in this project exist under two licenses illustrated more 
[here](https://www.riverbankcomputing.com/static/Docs/PyQt5/introduction.html#license).

PyQt4/5 can run in Windows, Linux, UNIX, Andorid and iOS platforms.

NOTE: PyQt4 was marked for deprecation therefore it would be advisable to use PyQt5 henceforth.

## Requirements

1. [Python 3](https://www.python.org/downloads/)
2. PyQt library

## Installation
#### Using pip in Windows
This assumes that you have already installed Python (python3) in this case which can be downloaded from 
[python website](https://www.python.org/downloads/).

Run command prompt in windows and first test if python is installed and exists in PATH by typing in the following 
command `python -version` or `python3 -version`

Then type `pip install pyqt5` to install PyQt5

#### Using pip in Linux(Ubuntu)
Check the python version using `python --version` or `python3 --version`

Then install PyQt5 using `pip install pyqt5`

#### Building from source
`sip-install`

`sip-install -h`

`
sip-build --no-make
make
make install
`

#### Building using PyQt bundle
`pyqt-bundle [options] wheel`


#### Linux distros
Ubuntu
`sudo apt-get install python3-pyqt5`

CentOS
`yum install qt5-qtbase-devel`

RPM-based systems like Redhat
`yum install PyQt5`

#### Mac OS X
Using brew in terminal type the command
`brew install pyqt`

## Chapters
### 1. [Hello World](001_HelloWorld)
### 2. [User Interfaces](002_User_interfaces)
### 3. [Layouts](003_Layouts)
### 4. [Events](004_Events)

