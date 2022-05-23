# Generated from Micro.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,9,5,2,0,7,0,1,0,1,0,1,0,0,0,1,0,0,0,3,0,2,1,0,0,0,2,3,1,0,0,
        0,3,1,1,0,0,0,0
    ]

class MicroParser ( Parser ):

    grammarFileName = "Micro.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\"'" ]

    symbolicNames = [ "<INVALID>", "INTLITERAL", "FLOATLITERAL", "KEYWORD", 
                      "IDENTIFIER", "QUOTE", "STRINGLITERAL", "OPERATOR", 
                      "COMMENT", "WS" ]

    RULE_useless = 0

    ruleNames =  [ "useless" ]

    EOF = Token.EOF
    INTLITERAL=1
    FLOATLITERAL=2
    KEYWORD=3
    IDENTIFIER=4
    QUOTE=5
    STRINGLITERAL=6
    OPERATOR=7
    COMMENT=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class UselessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MicroParser.RULE_useless

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUseless" ):
                listener.enterUseless(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUseless" ):
                listener.exitUseless(self)




    def useless(self):

        localctx = MicroParser.UselessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_useless)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





