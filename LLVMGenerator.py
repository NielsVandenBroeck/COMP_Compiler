class LLVMGenerator:
    def __init__(self,file_name, ast):
        self.file_name = file_name
        self.write(ast.getDot())

    def write(self, msg):
        with open(self.file_name, 'w') as myFile:
            myFile.write(msg)
