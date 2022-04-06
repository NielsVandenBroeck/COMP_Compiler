from AST import *
from grammar1Visitor import *
from SymbolTable import SymbolTable
from SemanticErrorAnalysis import SemanticErrorAnalysis

class ASTGenerator(grammar1Visitor):
    def __init__(self):
        self.variableList = []

    # Visit a parse tree produced by grammar1Parser#start.
    def visitStart(self, ctx):
        program = AST("program", ctx.start.line, ctx.start.column)
        for line in ctx.getChildren():
            if line.l is not None:
                object = self.visitChildren(line.l)
                if object is not None:
                    object.removePriority()
                    program.addNode(object)
            elif line.s is not None:
                program.addNode(self.visit(line.s))
        #SemanticErrorAnalysis(program)
        #symbolTable = SymbolTable(program)
        #symbolTable.checkUnusedVariables(program)
        return program

    # Visit a parse tree produced by grammar1Parser#IfStatement.
    def visitIfStatement(self, ctx):
        root = AST("if-else", ctx.start.line, ctx.start.column)
        conditionNode = AST("Condition", ctx.start.line, ctx.start.column)
        conditionBody = self.visit(ctx.b)
        conditionNode.addNode(conditionBody)
        root.addNode(conditionNode)
        ifScope = self.visit(ctx.s1)
        root.addNode(ifScope)
        if ctx.s2 is not None:
            elseScope = self.visit(ctx.s2)
            root.addNode(elseScope)
        return root

    # Visit a parse tree produced by grammar1Parser#WhileLoop.
    def visitWhileLoop(self, ctx):
        root = ASTWhile("while", ctx.start.line, ctx.start.column)
        conditionNode = ASTCondition("Condition", ctx.start.line, ctx.start.column)
        conditionBody = self.visit(ctx.b)
        conditionNode.addNode(conditionBody)
        root.addNode(conditionNode)
        whileScope = self.visit(ctx.s)
        root.addNode(whileScope)
        return root


    # Visit a parse tree produced by grammar1Parser#EmptyScope.
    def visitEmptyScope(self, ctx):
        root = ASTScope("Scope", ctx.start.line, ctx.start.column)
        for line in ctx.getChildren():
            if line.getChildCount() == 0:
                continue
            if line.l is not None:
                object = self.visitChildren(line.l)
                if object is not None:
                    object.removePriority()
                    root.addNode(object)
            elif line.s is not None:
                root.addNode(self.visitChildren(line))
        return root

    # Visit a parse tree produced by grammar1Parser#lvalue.
    def visitLvalue(self, ctx):
        lValue = ASTVariable(ctx.name.text, ctx.start.line, ctx.start.column)

        if ctx.pointer and ctx.t == None:
            lValue = ASTAdress(ASTAdress, ctx.start.line, ctx.start.column, [lValue])
            return ASTPointer(ASTPointer, ctx.start.line, ctx.start.column, [lValue])

        if ctx.t == None:
            return lValue

        if ctx.pointer != None:
            if ctx.t == None:
                lValue = ASTPointer(ASTPointer, ctx.start.line, ctx.start.column, [lValue])
                return lValue

            lValue = ASTDataType(ctx.t.getText(), ctx.start.line, ctx.start.column, [lValue])
            if ctx.constnessB != None:
                lValue = ASTConst("const",ctx.start.line, ctx.start.column, [lValue])
            lValue =  ASTPointer(ASTPointer, ctx.start.line, ctx.start.column, [lValue])
            if ctx.constnessA != None:
                lValue = ASTConst("const",ctx.start.line, ctx.start.column, [lValue])

        else:
            lValue = ASTDataType(ctx.t.getText(), ctx.start.line, ctx.start.column, [lValue])
            if ctx.constnessB != None:
                lValue = ASTConst("const", ctx.start.line, ctx.start.column, [lValue])
            if ctx.constnessA != None:
                lValue = ASTConst("const", ctx.start.line, ctx.start.column, [lValue])

        return lValue

    # Visit a parse tree produced by grammar1Parser#LValueRvalue.
    def visitLValueRvalue(self, ctx):
        node = self.visitLvalue(ctx.lv).removePriority()
        dataTypeNode = node.getFirstNonConst(node)
        dataTypeNode.addNode(self.visitRvalue(ctx.rv).removePriority())
        return node

    # Visit a parse tree produced by grammar1Parser#IdentifierOperationExpression.
    def visitIdentifierOperationExpression(self, ctx):
        name = ctx.name.text
        operation = ctx.op.getText()
        operation = operation[0]
        root = ASTVariable(name, ctx.start.line, ctx.start.column, [ASTOperator(operation, ctx.start.line, ctx.start.column, [ASTVariable(name, ctx.start.line, ctx.start.column), AST(1,  ctx.start.line, ctx.start.column)])])
        return root

    # Visit a parse tree produced by grammar1Parser#Printf.
    def visitPrintf(self, ctx):
        root = ASTPrintf("printf", ctx.start.line, ctx.start.column)
        root.addNode(self.visitChildren(ctx.b))
        return root

    # Visit a parse tree produced by grammar1Parser#unaryExpression.
    def visitUnaryExpression(self, ctx):
        sign = ctx.sign.text
        value = self.visit(ctx.value).removePriority()
        rootnode = ASTOperator(sign, ctx.start.line, ctx.start.column)
        rootnode.addNode(value)
        return rootnode

    # Visit a parse tree produced by grammar1Parser#OperationExpression.
    def visitOperationExpression(self, ctx):
        dict1 = {'||': 0, '&&': 1, '<': 2, '>': 2, '==': 2, '<=': 2, '>=': 2, '!=': 2, '+': 3, '-': 3, '*': 4, '/': 4, '%': 4}
        node1 = self.visit(ctx.lValue).removePriority()
        node2 = self.visit(ctx.rValue).removePriority()

        node2Priority = node2.isPriority()
        node2.removePriority()


        rootnode = self.visit(ctx.op)   #gaat naar visitOperation
        rootnode.addNode(node1)
        rootnode.addNode(node2)

        #len(node2.nodes) > 1 is voor unary getallen te onderscheiden van gewone
        if node2.root in dict1 and dict1[node2.root] < dict1[rootnode.root] and len(node2.nodes) > 1 and not node2Priority:
            tempNode2 = ASTOperator(rootnode.root, ctx.start.line, ctx.start.column)
            tempNode2.addNode(rootnode.getNode(0))
            tempNode2.addNode(node2.getNode(0))

            tempRootNode = ASTOperator(node2.root, ctx.start.line, ctx.start.column)
            tempRootNode.addNode(tempNode2)
            tempRootNode.addNode(node2.getNode(1))
            rootnode = tempRootNode

            node1 = tempNode2
            node2 = node2.getNode(1)
        elif node2Priority:
            node2 = None

        return rootnode

    # Visit a parse tree produced by grammar1Parser#ParenExpression.
    def visitParenExpression(self, ctx):
        rootnode = self.visit(ctx.value)
        return AST("()",ctx.start.line, ctx.start.column, [rootnode])

    # Visit a parse tree produced by grammar1Parser#IntExpression.
    def visitIntExpression(self, ctx):
        if ctx.getText()[0] == '!':
            tempNumber = int(ctx.getText()[1:len(ctx.getText())])
            if tempNumber:
                number = 0
            else: number = 1
        else: number = int(ctx.getText())
        return AST(number, ctx.start.line, ctx.start.column)

    # Visit a parse tree produced by grammar1Parser#FloatExpression.
    def visitFloatExpression(self, ctx):
        if ctx.getText()[0] == '!':
            tempNumber = float(ctx.getText()[1:len(ctx.getText())])
            if tempNumber:
                number = 0.0
            else: number = 1.0
        else: number = float(ctx.getText())
        return AST(number, ctx.start.line, ctx.start.column,)

    # Visit a parse tree produced by grammar1Parser#CharExpression.
    def visitCharExpression(self, ctx):
        char = ctx.getText()
        return AST(char, ctx.start.line, ctx.start.column,)

    # Visit a parse tree produced by grammar1Parser#VariableExpression.
    def visitVariableExpression(self, ctx):
        variable = ctx.getText()
        return ASTVariable(variable, ctx.start.line, ctx.start.column)

    # Visit a parse tree produced by grammar1Parser#operation.
    def visitOperation(self, ctx):
        operation = ctx.getText()
        return ASTOperator(operation, ctx.start.line, ctx.start.column)

    # Visit a parse tree produced by grammar1Parser#variableAdress.
    def visitVariableAdress(self, ctx):
        return ASTAdress(ASTAdress, ctx.start.line, ctx.start.column, [ASTVariable(ctx.name.text, ctx.start.line, ctx.start.column)])

    # Visit a parse tree produced by grammar1Parser#PointerValueExpression.
    def visitPointerValueExpression(self, ctx):
        return ASTPointer(ASTPointer, ctx.start.line, ctx.start.column, [ASTVariable(ctx.value.text, ctx.start.line, ctx.start.column)])
