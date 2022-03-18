class LLVMGenerator:
    def __init__(self,file_name, ast):
        self.file_name = file_name

    def write(self, msg):
        with open(self.file_name, 'w') as myFile:
            myFile.write(msg)
