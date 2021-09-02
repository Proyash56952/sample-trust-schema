from antlr4 import *
from TSPLexer import TSPLexer
from TSPListener import TSPListener
from TSPParser import TSPParser
from TSPVisitor import TSPVisitor
import sys

 
def main():
  istream = FileStream(sys.argv[1])
  lexer = TSPLexer(istream)
  stream = CommonTokenStream(lexer)
  parser = TSPParser(stream)
  tree = parser.policy()
  print(tree.toStringTree(recog=parser))
  

if __name__ == '__main__':
  main()
