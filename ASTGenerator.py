from AST import *
from grammar1Visitor import *
from SymbolTable import *
import copy
from ErrorAnalysis import ErrorAnalysis


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
                    object = object.removePriority()
                    program.addNode(object)
            elif line.s is not None:
                temp = self.visit(line.s)
                if type(temp) is ASTFor:
                    program.addNode(temp.nodes[0])
                    program.addNode(temp.nodes[1])
                else:
                    program.addNode(temp)
            elif line.f is not None:
                object = self.visit(line.f)
                if object is not None:
                    object = object.removePriority()
                    program.addNode(object)
            elif line.m is not None:
                temp = self.visit(line.m)
                if type(temp) is ASTMultiDeclaration:
                    for node in temp.nodes:
                        program.addNode(node)
        symbolTable = UpperSymbolTable(program)
        symbolTable.checkUnusedVariables(program)
        symbolTable.loopAST()
        ErrorAnalysis(program)

        return program

    # Visit a parse tree produced by grammar1Parser#function.
    def visitFunction(self, ctx):
        root = ASTFunction("Function", ctx.start.line, ctx.start.column)
        if ctx.t is not None:
            if ctx.pointer is not None:
                returnType = ASTDataType(ctx.t.getText(), ctx.start.line, ctx.start.column)
                returnType = ASTPointer(ASTPointer, ctx.start.line, ctx.start.column, [returnType])
            else:
                returnType = ASTDataType(ctx.t.getText(), ctx.start.line, ctx.start.column)
        else:
            returnType = ASTVoid("void", ctx.start.line, ctx.start.column)
        root.addNode(returnType)
        functionName = ctx.name.text
        functionName = ASTFunctionName(functionName, ctx.start.line, ctx.start.column)
        root.addNode(functionName)
        if ctx.p is not None:
            functionParams = self.visit(ctx.p)
            root.addNode(functionParams)
        functionScope = self.visit(ctx.s)
        root.addNode(functionScope)
        return root

    def visitFunctionForwardDeclaration(self, ctx):
        root = ASTForwardDeclaration("FunctionDeclaration", ctx.start.line, ctx.start.column)
        if ctx.t is not None:
            if ctx.pointer is not None:
                returnType = ASTDataType(ctx.t.getText(), ctx.start.line, ctx.start.column)
                returnType = ASTPointer(ASTPointer, ctx.start.line, ctx.start.column, [returnType])
            else:
                returnType = ASTDataType(ctx.t.getText(), ctx.start.line, ctx.start.column)
        else:
            returnType = ASTVoid("void", ctx.start.line, ctx.start.column)
        root.addNode(returnType)
        functionName = ctx.name.text
        functionName = ASTFunctionName(functionName, ctx.start.line, ctx.start.column)
        root.addNode(functionName)
        if ctx.p is not None:
            functionParams = self.visit(ctx.p)
            root.addNode(functionParams)
        return root

    # Visit a parse tree produced by grammar1Parser#params.
    def visitParams(self, ctx):
        root = ASTParameters("Parameters", ctx.start.line, ctx.start.column)
        for param in ctx.getChildren():
            if param.getChildCount() == 0:
                continue
            root.addNode(self.visit(param))
        return root

    # Visit a parse tree produced by grammar1Parser#IfStatement.
    def visitIfStatement(self, ctx):
        root = ASTIfElse("if-else", ctx.start.line, ctx.start.column)
        conditionNode = ASTCondition("Condition", ctx.start.line, ctx.start.column)
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

    # Visit a parse tree produced by grammar1Parser#ForLoop.
    def visitForLoop(self, ctx):
        root = ASTFor("", ctx.start.line, ctx.start.column)
        node1 = self.visitLvalue(ctx.lv).removePriority()
        dataTypeNode = node1.getFirstNonConst(node1)
        dataTypeNode.addNode(self.visitRvalue(ctx.rv).removePriority())

        node2 = ASTWhile("while", ctx.start.line, ctx.start.column)

        conditionNode = ASTCondition("Condition", ctx.start.line, ctx.start.column)
        conditionBody = self.visit(ctx.b)
        conditionNode.addNode(conditionBody)
        node2.addNode(conditionNode)
        whileScope = self.visit(ctx.s)
        node2.addNode(whileScope)

        node3 = self.visit(ctx.step)
        whileScope.addNode(node3)

        root.addNode(node1)
        root.addNode(node2)
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
                temp = self.visitChildren(line)
                if type(temp) is ASTFor:
                    root.addNode(temp.nodes[0])
                    root.addNode(temp.nodes[1])
                else:
                    root.addNode(temp)
            elif line.f is not None:
                exit("[Error] line: " + str(ctx.start.line) + ", position: " + str(
                    ctx.start.column) + ". Function definition is not allowed here.")
            elif line.m is not None:
                temp = self.visit(line.m)
                if type(temp) is ASTMultiDeclaration:
                    for node in temp.nodes:
                        root.addNode(node)
        return root

    # Visit a parse tree produced by grammar1Parser#param.
    def visitParam(self, ctx):
        lValue = ASTVariable(ctx.name.text, ctx.start.line, ctx.start.column)
        if ctx.pointer is not None:
            if ctx.t is None:
                lValue = ASTPointer(ASTPointer, ctx.start.line, ctx.start.column, [lValue])
                return lValue
            lValue = ASTDataType(ctx.t.getText(), ctx.start.line, ctx.start.column, [lValue])
            if ctx.constnessB is not None:
                lValue = ASTConst("const", ctx.start.line, ctx.start.column, [lValue])
            lValue = ASTPointer(ASTPointer, ctx.start.line, ctx.start.column, [lValue])
            if ctx.constnessA is not None:
                lValue = ASTConst("const", ctx.start.line, ctx.start.column, [lValue])
        else:
            lValue = ASTDataType(ctx.t.getText(), ctx.start.line, ctx.start.column, [lValue])
            if ctx.constnessB is not None:
                lValue = ASTConst("const", ctx.start.line, ctx.start.column, [lValue])
            if ctx.constnessA is not None:
                lValue = ASTConst("const", ctx.start.line, ctx.start.column, [lValue])

        if ctx.array is not None:
            lValue = ASTArray("Array", ctx.start.line, ctx.start.column, [lValue])
            index = ASTArrayLength("length", ctx.start.line, ctx.start.column)
            body = self.visit(ctx.array)
            index.addNode(body)
            lValue.addNode(index)
        return lValue

    # Visit a parse tree produced by grammar1Parser#multiAssignmentsDeclarations.
    def visitMultiAssignmentsDeclarations(self, ctx):
        root = ASTMultiDeclaration("multiDeclaration", ctx.start.line, ctx.start.column)
        dataType = self.getDataTypeForMultiDeclaration(ctx)

        if ctx.multidecl is not None:
            for declaration in ctx.multidecl.getChildren():
                if declaration.getChildCount() == 0:
                    continue
                UppernewDataType = copy.deepcopy(dataType)
                newdataType = UppernewDataType
                while newdataType.nodes is not None:
                    newdataType = newdataType.nodes[0]
                newdataType.addNode(
                    ASTVariable(declaration.name.text, declaration.start.line, declaration.start.column))
                if declaration.array is not None:
                    UppernewDataType = ASTArray("Array", declaration.start.line, declaration.start.column, [UppernewDataType])
                    index = ASTArrayLength("length", declaration.start.line, declaration.start.column)
                    body = self.visit(declaration.array)
                    index.addNode(body)
                    UppernewDataType.addNode(index)
                elif declaration.rval is not None:
                    rvalue = self.visit(declaration.rval)
                    UppernewDataType.getFirstNonConst(UppernewDataType).addNode(rvalue)
                root.addNode(UppernewDataType)
        return root

    def getDataTypeForMultiDeclaration(self, ctx):
        if ctx.pointer and ctx.t is None:
            dataType = ASTAdress(ASTAdress, ctx.start.line, ctx.start.column)
            return ASTPointer(ASTPointer, ctx.start.line, ctx.start.column, [dataType])

        if ctx.pointer is not None:
            if ctx.t is None:
                dataType = ASTPointer(ASTPointer, ctx.start.line, ctx.start.column)
                return dataType
            dataType = ASTDataType(ctx.t.getText(), ctx.start.line, ctx.start.column)
            if ctx.constnessB is not None:
                dataType = ASTConst("const", ctx.start.line, ctx.start.column, [dataType])
            dataType = ASTPointer(ASTPointer, ctx.start.line, ctx.start.column, [dataType])
            if ctx.constnessA is not None:
                dataType = ASTConst("const", ctx.start.line, ctx.start.column, [dataType])
        else:
            dataType = ASTDataType(ctx.t.getText(), ctx.start.line, ctx.start.column)
            if ctx.constnessB is not None:
                dataType = ASTConst("const", ctx.start.line, ctx.start.column, [dataType])
            if ctx.constnessA is not None:
                dataType = ASTConst("const", ctx.start.line, ctx.start.column, [dataType])
        return dataType

    # Visit a parse tree produced by grammar1Parser#lvalue.
    def visitLvalue(self, ctx):
        lValue = ASTVariable(ctx.name.text, ctx.start.line, ctx.start.column)
        if ctx.pointer and ctx.t is None:
            if ctx.array is not None:
                index = ASTArrayIndex('index', ctx.start.line, ctx.start.column)
                body = self.visit(ctx.array)
                index.addNode(body)
                lValue.addNode(index)
            lValue = ASTAdress(ASTAdress, ctx.start.line, ctx.start.column, [lValue])
            return ASTPointer(ASTPointer, ctx.start.line, ctx.start.column, [lValue])

        #assignment
        if ctx.t is None:
            if ctx.array is None:
                return lValue
            index = ASTArrayIndex('index', ctx.start.line, ctx.start.column)
            body = self.visit(ctx.array)
            index.addNode(body)
            lValue.addNode(index)
            return lValue

        #declaration
        if ctx.pointer is not None:
            lValue = ASTDataType(ctx.t.getText(), ctx.start.line, ctx.start.column, [lValue])
            if ctx.constnessB is not None:
                lValue = ASTConst("const", ctx.start.line, ctx.start.column, [lValue])
            lValue = ASTPointer(ASTPointer, ctx.start.line, ctx.start.column, [lValue])
            if ctx.constnessA is not None:
                lValue = ASTConst("const", ctx.start.line, ctx.start.column, [lValue])
        else:
            lValue = ASTDataType(ctx.t.getText(), ctx.start.line, ctx.start.column, [lValue])
            if ctx.constnessB is not None:
                lValue = ASTConst("const", ctx.start.line, ctx.start.column, [lValue])
            if ctx.constnessA is not None:
                lValue = ASTConst("const", ctx.start.line, ctx.start.column, [lValue])

        if ctx.array is not None:
            lValue = ASTArray("Array", ctx.start.line, ctx.start.column, [lValue])
            index = ASTArrayLength("length", ctx.start.line, ctx.start.column)
            body = self.visit(ctx.array)
            index.addNode(body)
            lValue.addNode(index)


        return lValue

    # Visit a parse tree produced by grammar1Parser#LValueRvalue.
    def visitLValueRvalue(self, ctx):
        node = self.visitLvalue(ctx.lv).removePriority()
        dataTypeNode = node.getFirstNonConst(node)
        dataTypeNode.addNode(self.visitRvalue(ctx.rv).removePriority())
        return node

    # Visit a parse tree produced by grammar1Parser#Printf.
    def visitPrintf(self, ctx):
        root = ASTPrintf("printf", ctx.start.line, ctx.start.column)
        root.addNode(ASTText(ctx.f.text.replace('"', ''), ctx.start.line, ctx.start.column))
        for body in ctx.pb.getChildren():
            if body.b is not None:
                root.addNode(self.visit(body.b))
        return root

    # Visit a parse tree produced by grammar1Parser#Scanf.
    def visitScanf(self, ctx):
        root = ASTScanf("scanf", ctx.start.line, ctx.start.column)
        root.addNode(ASTText(ctx.f.text.replace('"', ''), ctx.start.line, ctx.start.column))
        for variable in ctx.sv.getChildren():
            if variable.d is not None:
                root.addNode(self.visit(variable.d))
            elif variable.v is not None:
                root.addNode(self.visit(variable.v))
        return root

    # Visit a parse tree produced by grammar1Parser#OneTokenStatement.
    def visitOneTokenStatement(self, ctx):
        node = ASTOneTokenStatement(ctx.getText(), ctx.start.line, ctx.start.column)
        return node

    # Visit a parse tree produced by grammar1Parser#ReturnKeyword.
    def visitReturnKeyword(self, ctx):
        node = ASTReturn('return', ctx.start.line, ctx.start.column)
        if ctx.b is not None:
            node.addNode(self.visit(ctx.b))
        return node

    # Visit a parse tree produced by grammar1Parser#functionCall.
    def visitFunctionCall(self, ctx):
        root = ASTFunctionName(ctx.name.text, ctx.start.line, ctx.start.column)
        parameters = ASTParameters("Parameters", ctx.start.line, ctx.start.column)
        gotparam = False
        for param in ctx.getChildren():
            if param.getChildCount() == 0:
                continue
            else:
                gotparam = True
                parameters.addNode(self.visit(param))
        if gotparam:
            root.addNode(parameters)
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
        dict1 = {'||': 0, '&&': 1, '<': 2, '>': 2, '==': 2, '<=': 2, '>=': 2, '!=': 2, '+': 3, '-': 3, '*': 4, '/': 4,
                 '%': 4}
        node1 = self.visit(ctx.lValue).removePriority()
        node2 = self.visit(ctx.rValue).removePriority()

        node2Priority = node2.isPriority()
        node2.removePriority()

        rootnode = self.visit(ctx.op)  # gaat naar visitOperation
        rootnode.addNode(node1)
        rootnode.addNode(node2)

        # len(node2.nodes) > 1 is voor unary getallen te onderscheiden van gewone
        if node2.root in dict1 and dict1[node2.root] < dict1[rootnode.root] and len(
                node2.nodes) > 1 and not node2Priority:
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
        return AST("()", ctx.start.line, ctx.start.column, [rootnode])

    # Visit a parse tree produced by grammar1Parser#IntExpression.
    def visitIntExpression(self, ctx):
        number = int(ctx.getText())
        return ASTInt(number, ctx.start.line, ctx.start.column)

    # Visit a parse tree produced by grammar1Parser#FloatExpression.
    def visitFloatExpression(self, ctx):
        number = float(ctx.getText())
        return ASTFloat(number, ctx.start.line, ctx.start.column, )

    # Visit a parse tree produced by grammar1Parser#CharExpression.
    def visitCharExpression(self, ctx):
        char = ctx.getText()
        return ASTChar(char, ctx.start.line, ctx.start.column, )

    # Visit a parse tree produced by grammar1Parser#VariableExpression.
    def visitVariableExpression(self, ctx):
        variable = ASTVariable(ctx.value.text, ctx.start.line, ctx.start.column)
        if ctx.array is not None:
            index = ASTArrayIndex('index', ctx.start.line, ctx.start.column)
            body = self.visit(ctx.array)
            index.addNode(body)
            variable.addNode(index)
        return variable





        #if ctx.identifier is None:
        #    return ASTVariable(variable, ctx.start.line, ctx.start.column)
        #else:
        #    operation = ctx.identifier.getText()[0]
        #    root = ASTOperator(operation, ctx.start.line, ctx.start.column,
        #                       [ASTVariable(variable, ctx.start.line, ctx.start.column),
        #                        ASTInt(1, ctx.start.line, ctx.start.column)])
        #    return root

    # Visit a parse tree produced by grammar1Parser#negation.
    def visitNegation(self, ctx):
        negate = ASTOperator('!', ctx.start.line, ctx.start.column)
        negate.addNode(self.visit(ctx.b).removePriority())
        return negate

    # Visit a parse tree produced by grammar1Parser#operation.
    def visitOperation(self, ctx):
        operation = ctx.getText()
        return ASTOperator(operation, ctx.start.line, ctx.start.column)

    # Visit a parse tree produced by grammar1Parser#variableAdress.
    def visitVariableAdress(self, ctx):
        variable = ASTVariable(ctx.name.text, ctx.start.line, ctx.start.column)
        address = ASTAdress(ASTAdress, ctx.start.line, ctx.start.column,
                         [variable])
        if ctx.array is not None:
            index = ASTArrayIndex('index', ctx.start.line, ctx.start.column)
            body = self.visit(ctx.array)
            index.addNode(body)
            variable.addNode(index)
        return address

    # Visit a parse tree produced by grammar1Parser#PointerValueExpression.
    def visitPointerValueExpression(self, ctx):
        variable = ASTVariable(ctx.value.text, ctx.start.line, ctx.start.column)
        pointer = ASTPointer(ASTPointer, ctx.start.line, ctx.start.column, [variable])
        if ctx.array is not None:
            index = ASTArrayIndex('index', ctx.start.line, ctx.start.column)
            body = self.visit(ctx.array)
            index.addNode(body)
            variable.addNode(index)
        return pointer




        #if ctx.identifier is None:
        #    return ASTPointer(ASTPointer, ctx.start.line, ctx.start.column,
        #                      [ASTVariable(ctx.value.text, ctx.start.line, ctx.start.column)])
        #else:
        #    operation = ctx.identifier.getText()[0]
        #    root = ASTOperator(operation, ctx.start.line, ctx.start.column,
        #                       [ASTPointer(ASTPointer, ctx.start.line, ctx.start.column,
        #                                   [ASTVariable(ctx.value.text, ctx.start.line, ctx.start.column)]),
        #                        ASTInt(1, ctx.start.line, ctx.start.column)])
        #    return root
