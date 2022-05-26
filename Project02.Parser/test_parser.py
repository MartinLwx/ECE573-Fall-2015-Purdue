import sys
from antlr4 import *
from MicroLexer import MicroLexer
from MicroParser import MicroParser

def main(argv):
    input_stream = FileStream(argv)
    lexer = MicroLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MicroParser(token_stream)
    # remove the error output
    parser.removeErrorListeners()
    # begin to parse the input file
    tree = parser.program()
    # count the syntaxError
    cnt = parser.getNumberOfSyntaxErrors()
    if cnt == 0:
        print("Accepted")
    else:
        print("Not accepted")
    

if __name__ == "__main__":
    main(sys.argv[1])
