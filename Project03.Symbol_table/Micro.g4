grammar Micro;

@parser::members {

def init(self):
    self.current_scope = None
    self.block_count = 0
    self.warning_list = []
    self.output_list = []
    self.declaration_error = ''
    
def enter_new_scope(self):
    if not hasattr(self, '_scopes'):
        setattr(self, '_scopes', [])
    # save the current_scope
    import copy
    if len(self._scopes) > 0:
        self._scopes.append(copy.deepcopy(self.current_scope))
    self._scopes.append({})
    self.current_scope =  self._scopes[-1]
    #print(f"len: {len(self._scopes)}")

def exit_scope(self):
    del self._scopes[-1]
    if len(self._scopes) > 0:
        self.current_scope =  self._scopes[-1]

def lookup(self, identifier, value):
    #print(f"---> level: {len(self._scopes)}, {identifier}={value}")
    # check all scopes
    found = False
    for scope in self._scopes[:-1][::-1]:
        #print(f"the scope: {scope}")
        if identifier in scope:
            found = True
    if found:
        self.warning_list.append(f"SHADOW WARNING {identifier}")
    # only record the 1st declaration error
    if identifier in self.current_scope and self.declaration_error == '':
        self.declaration_error = f"DECLARATION ERROR {identifier}"
    self.current_scope[identifier] = value
    #print(f"---> current scope: {self.current_scope}")
}


/* Program */
program :   'PROGRAM' 
        {
self.init()
self.output_list.append("Symbol table GLOBAL")
self.enter_new_scope()
        }   id 'BEGIN' pgm_body 'END' 
        {
self.exit_scope()
# output everything after we parsing this program
if self.declaration_error != '':
    print(self.declaration_error)
else:
    if len(self.warning_list) > 0:
        print('\n'.join(self.warning_list))
    print('\n'.join(self.output_list))
        }
        ;
id      :   IDENTIFIER;
pgm_body:   decl func_declarations ;
decl    :   string_decl decl 
        |   var_decl decl 
        | 
        ;

/* Global String Declaration */
string_decl :   'STRING' id ':=' str ';' 
            {
self.lookup($id.text, $str.text)
self.output_list.append(f"name {$id.text} type STRING value {$str.text}")
            }
;
str         :   STRINGLITERAL ;

/* Variable Declaration */
// We only have FLOAT && INT && VOID in the Micro language
var_decl    :   var_type id_list ';' 
            {
# NOTE: the indentation is correct, ANLTR4 will handle this for us :)
# for all variable declarations, we should output the name && type

# in the same variable declaration, it means all of the variables have the same type
for variable in $id_list.text.split(','):
    self.lookup(variable, None)
    self.output_list.append(f"name {variable} type {$var_type.text}")
            }
            ; 
var_type    :   'FLOAT'              
            |   'INT' 
            ;          
any_type    :   var_type 
            |   'VOID' 
            ;
id_list     :   id id_tail ;
id_tail     :   ',' id id_tail 
            | 
            ;

/* Function Paramater List */
param_decl_list     :   param_decl param_decl_tail 
                    | 
                    ;
param_decl          :   var_type id 
                    {
self.lookup($id.text, None)
self.output_list.append(f"name {$id.text} type {$var_type.text}")
                    }
                    ;
param_decl_tail     :   ',' param_decl param_decl_tail 
                    | 
                    ;


/* Function Declarations */
func_declarations   :   func_decl func_declarations 
                    | 
                    ;
func_decl           :   'FUNCTION' any_type id 
                    {
# print a newline before entering the new scope
self.output_list.append('')
self.output_list.append(f"Symbol table {$id.text}")
self.enter_new_scope()
                    }   '(' param_decl_list ')' 'BEGIN' func_body 'END' {self.exit_scope()} ;
func_body           :   decl stmt_list ;

/* Statement List */
stmt_list           :   stmt stmt_list 
                    | 
                    ;
stmt                :   base_stmt 
                    |   if_stmt 
                    |   for_stmt
                    ;
base_stmt           :   assign_stmt 
                    |   read_stmt 
                    |   write_stmt 
                    |   return_stmt
                    ;

/* Basic Statements */
assign_stmt         :   assign_expr ';' ;
assign_expr         :   id ':=' expr ;
read_stmt           :   'READ' '(' id_list ')' ';' ;
write_stmt          :   'WRITE' '(' id_list ')' ';' ;
return_stmt         :   'RETURN' expr ';' ;

/* Expressions */
expr                :   expr_prefix factor ;
expr_prefix         :   expr_prefix factor addop 
                    | 
                    ;
factor              :   factor_prefix postfix_expr;
factor_prefix       :   factor_prefix postfix_expr mulop 
                    | 
                    ;
postfix_expr        :   primary 
                    |   call_expr
                    ;
call_expr           :   id '(' expr_list ')' ;
expr_list           :   expr expr_list_tail 
                    | 
                    ;
expr_list_tail      :   ',' expr expr_list_tail 
                    | 
                    ;
primary             :   '(' expr ')' 
                    |   id 
                    |   INTLITERAL 
                    |   FLOATLITERAL;
addop               :   '+' 
                    |   '-'
                    ;
mulop               :   '*' 
                    |   '/'
                    ;

/* Complex Statements and Condition */ 
// we don't use {...} to for a code blcok
if_stmt             :   'IF' '(' cond ')' 
                    {
self.block_count += 1
self.enter_new_scope()
self.output_list.append('')
self.output_list.append(f"Symbol table BLOCK {self.block_count}")
                    }
                        decl stmt_list {self.exit_scope()} else_part 'FI' ;
else_part           :   'ELSE' 
                    {
self.block_count += 1
self.enter_new_scope()
self.output_list.append('')
self.output_list.append(f"Symbol table BLOCK {self.block_count}")
                    }
                        decl stmt_list {self.exit_scope()}
                    | 
                    ;
cond                :   expr compop expr;
compop              :   '<' 
                    |   '>' 
                    |   '=' 
                    |   '!=' 
                    |   '<=' 
                    |   '>='
                    ;

init_stmt           :   assign_expr 
                    | 
                    ;
incr_stmt           :   assign_expr 
                    | 
                    ;

/* ECE 573 students use this version of for_stmt */
for_stmt            :   'FOR' '(' init_stmt ';' cond ';' incr_stmt ')' 
                    {
self.block_count += 1
self.enter_new_scope()
self.output_list.append('')
self.output_list.append(f"Symbol table BLOCK {self.block_count}")
                    }
                        decl aug_stmt_list 'ROF' {self.exit_scope()};

/* CONTINUE and BREAK statements. ECE 573 students only */
aug_stmt_list       :   aug_stmt aug_stmt_list 
                    | 
                    ;
// change if_stmt -> aug_if_stmt
aug_stmt            :   base_stmt 
                    |   aug_if_stmt 
                    |   for_stmt 
                    |   'CONTINUE' ';' 
                    |   'BREAK' ';' 
                    ;

/* Augmented IF statements for ECE 573 students */ 
aug_if_stmt         :   'IF' '(' cond ')' 
                    {
self.block_count += 1
self.enter_new_scope()
self.output_list.append('')
self.output_list.append(f"Symbol table BLOCK {self.block_count}")
                    }
                        decl aug_stmt_list {self.exit_scope()} aug_else_part 'FI' ;
aug_else_part       :   'ELSE' 
                    {
self.block_count += 1
self.enter_new_scope()
self.output_list.append('')
self.output_list.append(f"Symbol table BLOCK {self.block_count}")
                    }
                    decl aug_stmt_list
                    | {self.exit_scope()}
                    ;

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
