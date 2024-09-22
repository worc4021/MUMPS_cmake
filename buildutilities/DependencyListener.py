from Graph import Graph
from makeParser import makeParser
from makeListener import makeListener

class DependencyListener(makeListener):
    def __init__(self):
        self.graph = Graph()
        self.variables = Graph()
        self.current_node = None
        self.current_var = None
    def exitTarget(self, ctx: makeParser.TargetContext):
        self.current_node = ctx.getText()

    def exitUsefulDependent(self, ctx: makeParser.UsefulDependentContext):
        if not self.graph.has_node(self.current_node):
            self.graph.add_node(self.current_node)
        if not self.graph.has_node(ctx.getText()):
            self.graph.add_node(ctx.getText())
        
        self.graph.add_edge(self.current_node, ctx.getText())

    def exitVarname(self, ctx: makeParser.VarnameContext):
        self.current_var = "$(" + ctx.getText() + ")"

    def exitUsefulAssignee(self, ctx: makeParser.UsefulAssigneeContext):
        if not self.variables.has_node(self.current_var):
            self.variables.add_node(self.current_var)
        if not self.variables.has_node(ctx.getText()):
            self.variables.add_node(ctx.getText())
        
        self.variables.add_edge(self.current_var, ctx.getText())

    def getGraph(self):
        return self.graph