from antlr4 import *
from demoLexer import demoLexer
from demoListener import demoListener
from demoParser import demoParser
from demoVisitor import demoVisitor
import sys

 
def main():
  istream = FileStream(sys.argv[1])
  lexer = demoLexer(istream)
  stream = CommonTokenStream(lexer)
  parser = demoParser(stream)
  tree = parser.st()
  print(tree.toStringTree(recog=parser))
  

if __name__ == '__main__':
  main()
