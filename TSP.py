from antlr4 import *
from TSPLexer import TSPLexer
from TSPListener import TSPListener
from TSPParser import TSPParser
from TSPVisitor import TSPVisitor
import sys

class CustomVisitor(TSPVisitor):
  def __init__(self):
    self.policies = {}

  def visitPolicy_statement(self,ctx):
    self.policies[ctx.location().getText()] = ctx.device().getText()
    print(ctx.location.getText())
  def show(self):
    for (i,j) in self.policies:
    	print(i,j)
 
def main():
  istream = FileStream(sys.argv[1])
  lexer = TSPLexer(istream)
  stream = CommonTokenStream(lexer)
  parser = TSPParser(stream)
  tree = parser.policy()
  print(tree.toStringTree(recog=parser))
  
  visitor = CustomVisitor()
  visitor.visit(tree)
  #visitor.show()
if __name__ == '__main__':
  main()
