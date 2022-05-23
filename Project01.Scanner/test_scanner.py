import sys
from antlr4 import *
from MicroLexer import MicroLexer



def main(argv):
	# 这里指的是 CharStream
    input_stream = FileStream(argv[1])
    lexer = MicroLexer(input_stream)
    tokens = lexer.getAllTokens()
    vocab = MicroLexer.symbolicNames

    res = []
    for token in tokens:
        # the `token.type` is an integer, we need to convert it to the real name :)
        token_type = vocab[token.type]
        token_value = token.text
        res.append(f"Token Type: {token_type}")
        res.append(f"Value: {token_value}")
    final_string = '\n'.join(res)
    print(final_string)


if __name__ == '__main__':
    main(sys.argv)
