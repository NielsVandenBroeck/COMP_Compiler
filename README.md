# README #
Compiler From Stein Vandenbroeke and Niels Van den Broeck

### Features ###
 - Parsing mathematical expressions
 - Parsing a subset of C language
   - Variable declarations and initializations
   - Datatypes
     - int
     - float
     - char
     - pointer
   - Comments
   - Printf()
 - Translating to an Abstract syntax tree
 - Error analysis

### How to use ###
To compile some C code, add your C-file as an argument to the program. 
As return, a dot file will be created in the OutputFiles map to visualize the constructed Abstract syntax tree. 
Later on, You will find the converted LLVM code in the same directory.

