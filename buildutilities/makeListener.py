# Generated from ./make.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .makeParser import makeParser
else:
    from makeParser import makeParser

# This class defines a complete listener for a parse tree produced by makeParser.
class makeListener(ParseTreeListener):

    # Enter a parse tree produced by makeParser#file.
    def enterFile(self, ctx:makeParser.FileContext):
        pass

    # Exit a parse tree produced by makeParser#file.
    def exitFile(self, ctx:makeParser.FileContext):
        pass


    # Enter a parse tree produced by makeParser#content.
    def enterContent(self, ctx:makeParser.ContentContext):
        pass

    # Exit a parse tree produced by makeParser#content.
    def exitContent(self, ctx:makeParser.ContentContext):
        pass


    # Enter a parse tree produced by makeParser#specialRecipe.
    def enterSpecialRecipe(self, ctx:makeParser.SpecialRecipeContext):
        pass

    # Exit a parse tree produced by makeParser#specialRecipe.
    def exitSpecialRecipe(self, ctx:makeParser.SpecialRecipeContext):
        pass


    # Enter a parse tree produced by makeParser#regularRecipe.
    def enterRegularRecipe(self, ctx:makeParser.RegularRecipeContext):
        pass

    # Exit a parse tree produced by makeParser#regularRecipe.
    def exitRegularRecipe(self, ctx:makeParser.RegularRecipeContext):
        pass


    # Enter a parse tree produced by makeParser#target.
    def enterTarget(self, ctx:makeParser.TargetContext):
        pass

    # Exit a parse tree produced by makeParser#target.
    def exitTarget(self, ctx:makeParser.TargetContext):
        pass


    # Enter a parse tree produced by makeParser#dependents.
    def enterDependents(self, ctx:makeParser.DependentsContext):
        pass

    # Exit a parse tree produced by makeParser#dependents.
    def exitDependents(self, ctx:makeParser.DependentsContext):
        pass


    # Enter a parse tree produced by makeParser#usefulDependent.
    def enterUsefulDependent(self, ctx:makeParser.UsefulDependentContext):
        pass

    # Exit a parse tree produced by makeParser#usefulDependent.
    def exitUsefulDependent(self, ctx:makeParser.UsefulDependentContext):
        pass


    # Enter a parse tree produced by makeParser#uselessDependent.
    def enterUselessDependent(self, ctx:makeParser.UselessDependentContext):
        pass

    # Exit a parse tree produced by makeParser#uselessDependent.
    def exitUselessDependent(self, ctx:makeParser.UselessDependentContext):
        pass


    # Enter a parse tree produced by makeParser#assignment.
    def enterAssignment(self, ctx:makeParser.AssignmentContext):
        pass

    # Exit a parse tree produced by makeParser#assignment.
    def exitAssignment(self, ctx:makeParser.AssignmentContext):
        pass


    # Enter a parse tree produced by makeParser#varname.
    def enterVarname(self, ctx:makeParser.VarnameContext):
        pass

    # Exit a parse tree produced by makeParser#varname.
    def exitVarname(self, ctx:makeParser.VarnameContext):
        pass


    # Enter a parse tree produced by makeParser#uselessAssignee.
    def enterUselessAssignee(self, ctx:makeParser.UselessAssigneeContext):
        pass

    # Exit a parse tree produced by makeParser#uselessAssignee.
    def exitUselessAssignee(self, ctx:makeParser.UselessAssigneeContext):
        pass


    # Enter a parse tree produced by makeParser#usefulAssignee.
    def enterUsefulAssignee(self, ctx:makeParser.UsefulAssigneeContext):
        pass

    # Exit a parse tree produced by makeParser#usefulAssignee.
    def exitUsefulAssignee(self, ctx:makeParser.UsefulAssigneeContext):
        pass


    # Enter a parse tree produced by makeParser#continued.
    def enterContinued(self, ctx:makeParser.ContinuedContext):
        pass

    # Exit a parse tree produced by makeParser#continued.
    def exitContinued(self, ctx:makeParser.ContinuedContext):
        pass


    # Enter a parse tree produced by makeParser#commands.
    def enterCommands(self, ctx:makeParser.CommandsContext):
        pass

    # Exit a parse tree produced by makeParser#commands.
    def exitCommands(self, ctx:makeParser.CommandsContext):
        pass


    # Enter a parse tree produced by makeParser#command.
    def enterCommand(self, ctx:makeParser.CommandContext):
        pass

    # Exit a parse tree produced by makeParser#command.
    def exitCommand(self, ctx:makeParser.CommandContext):
        pass


    # Enter a parse tree produced by makeParser#filename.
    def enterFilename(self, ctx:makeParser.FilenameContext):
        pass

    # Exit a parse tree produced by makeParser#filename.
    def exitFilename(self, ctx:makeParser.FilenameContext):
        pass



del makeParser