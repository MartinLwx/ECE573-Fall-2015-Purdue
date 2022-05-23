grammar Micro;

// just ignore the nonsense, the ANTLR requires at least one rule
useless         :   ;

fragment DIGIT  :   [0-9];
fragment LETTER :   [a-zA-Z];
INTLITERAL      :   DIGIT+;
FLOATLITERAL    :   DIGIT*'.'DIGIT+;

// the KEYWORD token should appear before the IDENTIFIER
KEYWORD         :   'PROGRAM' 
                |   'BEGIN' 
                |   'END' 
                |   'FUNCTION' 
                |   'READ' 
                |   'WRITE' 
                |   'IF' 
                |   'ELSE' 
                |   'FI' 
                |   'FOR' 
                |   'ROF' 
                |   'CONTINUE' 
                |   'BREAK' 
                |   'RETURN' 
                |   'INT' 
                |   'VOID' 
                |   'STRING' 
                |   'FLOAT'
                ;
IDENTIFIER      :   LETTER [0-9a-zA-Z]*;
QUOTE           :   '"';
STRINGLITERAL   :   QUOTE .*? QUOTE;
OPERATOR        :   ':=' 
                |   '+' 
                |   '-' 
                |   '*' 
                |   '/' 
                |   '=' 
                |   '!=' 
                |   '<' 
                |   '>' 
                |   '(' 
                |   ')' 
                |   ';' 
                |   ',' 
                |   '<=' 
                |   '>='
                ;
COMMENT         :   '--' ~[\n\r]* -> skip;

WS              :   [ \t\n\r] -> skip;
