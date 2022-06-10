# README #
Compiler From Stein Vandenbroeke and Niels Van den Broeck

### Implemented Features ###
- Project 1
  - (mandatory) Binary operations +, -, *, and /.
  - (mandatory) Binary operations >, <, and ==.
  - (mandatory) Unary operators + and -.
  - (mandatory) Brackets to overwrite the order of operations.
  - (mandatory) Logical operators &&, ||, and !.
  - (optional) Comparison operators >=, <=, and !=.
  - (optional) Binary operator %. 
  
- Project 2
  - (mandatory) Types: char, float, int and pointer.
  - (mandatory) Reserved word const keyword.
  - (mandatory) Variables: declarations, definitions, assignment statements and identifiers appearing in expressions.
  - (mandatory) Pointer Operations * and &.
  - (optional) Identifier Operations ++ and --.
  - (optional) Type Conversions. 
  
- Project 3
  - (mandatory) Single line Comments and multiline comments.
  - (mandatory) Printf.
  
- Project 4
  - (mandatory) Reserved words if, else, and while.
  - (mandatory) for.
  - (mandatory) break.
  - (mandatory) continue.
  - (mandatory) Scopes.

- Project 5
  - (mandatory) Reserved words return and void.
  - (mandatory) Scopes.
  - (mandatory) Local and global variables.
  - (mandatory) Functions.
  - (mandatory) Unreachable code and dead code.
  - (mandatory) If you support the break or continue keywords, do not generate
code for statements that appear after these keywords in a loop.

- Project 6
  - (mandatory) Arrays.
  - (mandatory) printf and scanf.


### How to install ###
To run the program python3 is needed.

First create a env:
```bash
virtualenv -p python3 env
````
Now open the env
```bash
source env/bin/activate
````
Install all needed libraries
```bash
pip3 install -r requirements.txt
````

if you would like to run all

### How to use ###
run one of the line below, depending on what language and which files you want to run the compiler on
```bash
python main.py llvm True/False file/folder		::([0]=language, [1]=run program after compile, [2]=file/folder location)
````
```bash
python main.py mips True/False file/folder		::([0]=language, [1]=run program after compile, [2]=file/folder location)
````

As return, a dot file and llvm/mips file will be created in the OutputFiles map for every compiled file.

