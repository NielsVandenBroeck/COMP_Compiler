from AST import ASTVariable


class ASTFold:
    def __init__(self, ast):
        return

    def innorderTraverseAndFold(self, ast):
        if(type(ast) == ASTVariable):
            ast.constantFold()