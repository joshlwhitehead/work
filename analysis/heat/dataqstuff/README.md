# Data Acquisition Visualizer/Evaluator (DAVE)

## General Info

This is a python tool for plotting log data from the YouTest runs

## Requirements

If you intend to build the app from source or contribute to the project, you
will need the following tools (and their respective dependencies) installed:
- [Python] 3.5+
- [PyInstaller]

[Python]: https://www.python.org
[PyInstaller]: http://www.pyinstaller.org

## Setup Info
Run the following to install all python package dependencies:
```
pip install -r requirements.txt
```
## Build Info
To build executables run the following
```
pyinstaller --onefile main.spec
```
This will generate a new executable in `dist`

## Running
You can run the program by calling `python main.py`.