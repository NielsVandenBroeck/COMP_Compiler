# README #
Compiler From Stein Vandenbroeke and Niels Van den Broeck

### Mandatory Features ###
 - Parsing mathematical expressions
 - Parsing a subset of C language
   - Variable declarations and initializations
   - Datatypes with operations
     - int
     - float
     - char
     - pointer
   - Comments
   - Printf() and scanf()
   - If, else, while, for, break, continue
   - scopes
   - Functions
   - Local and global variables
   - unreachable and dead code
 - Translating to an Abstract syntax tree
 - Error analysis
 - Translating above features to LLVM

### Not yet implemented Mandatory Features ###
- Arrays
- Import Files (scanf and printf do work)

### Optional Features ###
- Comparison operators >=, <=, and !=
- Binary operator %
- Conversions (float isRicherThan int isRicherThan char)


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

### How to use ###
To compile some C code, add your C-file as an argument to the program. 
As return, a dot file will be created in the OutputFiles map to visualize the constructed Abstract syntax tree. 
Later on, You will find the converted LLVM code in the same directory.

```bash
python main.py inputfile.txt
````
