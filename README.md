# Recursivity

This repository contains a python application that prints out the pascal triangle in the commandline for an arbitrary level. 

The main objectives: 

* Demonstrate how to create commandline application in python. 
* Use two different paradigms for application design: object-oriented and functional programming. 
* Use python best practices and common patterns (e.g. logging library, decorators, lambdas)

## Setup

Clone this repository and do the following:

1. Create and activate a virtualenv
    * `virtualenv --python=python3 venv`
    * `source venv/bin/activate`
1. Install requirements
    * `pip install -r requirements.txt`

## Usage

Once `venv` in active, the usage is fairly simple: 

```commandline
$ python main.py pascal_triangle --level 5 --option a
```

Options: 

```text
    --level  : a positive integer indicating the total number of rows. 
    --option : custom implementation with possible values {a, b}
```

## Examples

Pascal traingle with 5 rows using implementation a:

```text
$ python main.py pascal_triangle --level 5 --option b
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
INFO:__main__:Execution time 0.0002219676971435547
```

Pascal triangle with 15 rows using implementation b: 

```text
$ python main.py pascal_triangle --level 15 --option a
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
1 7 21 35 35 21 7 1
1 8 28 56 70 56 28 8 1
1 9 36 84 126 126 84 36 9 1
1 10 45 120 210 252 210 120 45 10 1
1 11 55 165 330 462 462 330 165 55 11 1
1 12 66 220 495 792 924 792 495 220 66 12 1
1 13 78 286 715 1287 1716 1716 1287 715 286 78 13 1
1 14 91 364 1001 2002 3003 3432 3003 2002 1001 364 91 14 1
INFO:__main__:Execution time 0.0006437301635742188
```