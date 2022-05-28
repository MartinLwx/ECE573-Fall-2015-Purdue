import sys
from antlr4 import *
from MicroLexer import MicroLexer
from MicroParser import MicroParser

def main(argv):
    char_stream = FileStream(argv)
    lexer = MicroLexer(char_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MicroParser(token_stream)
    tree = parser.program()


if __name__ == "__main__":
    main(sys.argv[1])