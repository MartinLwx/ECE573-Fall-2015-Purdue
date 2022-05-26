# Generated from Micro.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MicroParser import MicroParser
else:
    from MicroParser import MicroParser

# This class defines a complete listener for a parse tree produced by MicroParser.
class MicroListener(ParseTreeListener):

    # Enter a parse tree produced by MicroParser#program.
    def enterProgram(self, ctx:MicroParser.ProgramContext):
        pass

    # Exit a parse tree produced by MicroParser#program.
    def exitProgram(self, ctx:MicroParser.ProgramContext):
        pass


    # Enter a parse tree produced by MicroParser#id.
    def enterId(self, ctx:MicroParser.IdContext):
        pass

    # Exit a parse tree produced by MicroParser#id.
    def exitId(self, ctx:MicroParser.IdContext):
        pass


    # Enter a parse tree produced by MicroParser#pgm_body.
    def enterPgm_body(self, ctx:MicroParser.Pgm_bodyContext):
        pass

    # Exit a parse tree produced by MicroParser#pgm_body.
    def exitPgm_body(self, ctx:MicroParser.Pgm_bodyContext):
        pass


    # Enter a parse tree produced by MicroParser#decl.
    def enterDecl(self, ctx:MicroParser.DeclContext):
        pass

    # Exit a parse tree produced by MicroParser#decl.
    def exitDecl(self, ctx:MicroParser.DeclContext):
        pass


    # Enter a parse tree produced by MicroParser#string_decl.
    def enterString_decl(self, ctx:MicroParser.String_declContext):
        pass

    # Exit a parse tree produced by MicroParser#string_decl.
    def exitString_decl(self, ctx:MicroParser.String_declContext):
        pass


    # Enter a parse tree produced by MicroParser#str.
    def enterStr(self, ctx:MicroParser.StrContext):
        pass

    # Exit a parse tree produced by MicroParser#str.
    def exitStr(self, ctx:MicroParser.StrContext):
        pass


    # Enter a parse tree produced by MicroParser#var_decl.
    def enterVar_decl(self, ctx:MicroParser.Var_declContext):
        pass

    # Exit a parse tree produced by MicroParser#var_decl.
    def exitVar_decl(self, ctx:MicroParser.Var_declContext):
        pass


    # Enter a parse tree produced by MicroParser#var_type.
    def enterVar_type(self, ctx:MicroParser.Var_typeContext):
        pass

    # Exit a parse tree produced by MicroParser#var_type.
    def exitVar_type(self, ctx:MicroParser.Var_typeContext):
        pass


    # Enter a parse tree produced by MicroParser#any_type.
    def enterAny_type(self, ctx:MicroParser.Any_typeContext):
        pass

    # Exit a parse tree produced by MicroParser#any_type.
    def exitAny_type(self, ctx:MicroParser.Any_typeContext):
        pass


    # Enter a parse tree produced by MicroParser#id_list.
    def enterId_list(self, ctx:MicroParser.Id_listContext):
        pass

    # Exit a parse tree produced by MicroParser#id_list.
    def exitId_list(self, ctx:MicroParser.Id_listContext):
        pass


    # Enter a parse tree produced by MicroParser#id_tail.
    def enterId_tail(self, ctx:MicroParser.Id_tailContext):
        pass

    # Exit a parse tree produced by MicroParser#id_tail.
    def exitId_tail(self, ctx:MicroParser.Id_tailContext):
        pass


    # Enter a parse tree produced by MicroParser#param_decl_list.
    def enterParam_decl_list(self, ctx:MicroParser.Param_decl_listContext):
        pass

    # Exit a parse tree produced by MicroParser#param_decl_list.
    def exitParam_decl_list(self, ctx:MicroParser.Param_decl_listContext):
        pass


    # Enter a parse tree produced by MicroParser#param_decl.
    def enterParam_decl(self, ctx:MicroParser.Param_declContext):
        pass

    # Exit a parse tree produced by MicroParser#param_decl.
    def exitParam_decl(self, ctx:MicroParser.Param_declContext):
        pass


    # Enter a parse tree produced by MicroParser#param_decl_tail.
    def enterParam_decl_tail(self, ctx:MicroParser.Param_decl_tailContext):
        pass

    # Exit a parse tree produced by MicroParser#param_decl_tail.
    def exitParam_decl_tail(self, ctx:MicroParser.Param_decl_tailContext):
        pass


    # Enter a parse tree produced by MicroParser#func_declarations.
    def enterFunc_declarations(self, ctx:MicroParser.Func_declarationsContext):
        pass

    # Exit a parse tree produced by MicroParser#func_declarations.
    def exitFunc_declarations(self, ctx:MicroParser.Func_declarationsContext):
        pass


    # Enter a parse tree produced by MicroParser#func_decl.
    def enterFunc_decl(self, ctx:MicroParser.Func_declContext):
        pass

    # Exit a parse tree produced by MicroParser#func_decl.
    def exitFunc_decl(self, ctx:MicroParser.Func_declContext):
        pass


    # Enter a parse tree produced by MicroParser#func_body.
    def enterFunc_body(self, ctx:MicroParser.Func_bodyContext):
        pass

    # Exit a parse tree produced by MicroParser#func_body.
    def exitFunc_body(self, ctx:MicroParser.Func_bodyContext):
        pass


    # Enter a parse tree produced by MicroParser#stmt_list.
    def enterStmt_list(self, ctx:MicroParser.Stmt_listContext):
        pass

    # Exit a parse tree produced by MicroParser#stmt_list.
    def exitStmt_list(self, ctx:MicroParser.Stmt_listContext):
        pass


    # Enter a parse tree produced by MicroParser#stmt.
    def enterStmt(self, ctx:MicroParser.StmtContext):
        pass

    # Exit a parse tree produced by MicroParser#stmt.
    def exitStmt(self, ctx:MicroParser.StmtContext):
        pass


    # Enter a parse tree produced by MicroParser#base_stmt.
    def enterBase_stmt(self, ctx:MicroParser.Base_stmtContext):
        pass

    # Exit a parse tree produced by MicroParser#base_stmt.
    def exitBase_stmt(self, ctx:MicroParser.Base_stmtContext):
        pass


    # Enter a parse tree produced by MicroParser#assign_stmt.
    def enterAssign_stmt(self, ctx:MicroParser.Assign_stmtContext):
        pass

    # Exit a parse tree produced by MicroParser#assign_stmt.
    def exitAssign_stmt(self, ctx:MicroParser.Assign_stmtContext):
        pass


    # Enter a parse tree produced by MicroParser#assign_expr.
    def enterAssign_expr(self, ctx:MicroParser.Assign_exprContext):
        pass

    # Exit a parse tree produced by MicroParser#assign_expr.
    def exitAssign_expr(self, ctx:MicroParser.Assign_exprContext):
        pass


    # Enter a parse tree produced by MicroParser#read_stmt.
    def enterRead_stmt(self, ctx:MicroParser.Read_stmtContext):
        pass

    # Exit a parse tree produced by MicroParser#read_stmt.
    def exitRead_stmt(self, ctx:MicroParser.Read_stmtContext):
        pass


    # Enter a parse tree produced by MicroParser#write_stmt.
    def enterWrite_stmt(self, ctx:MicroParser.Write_stmtContext):
        pass

    # Exit a parse tree produced by MicroParser#write_stmt.
    def exitWrite_stmt(self, ctx:MicroParser.Write_stmtContext):
        pass


    # Enter a parse tree produced by MicroParser#return_stmt.
    def enterReturn_stmt(self, ctx:MicroParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by MicroParser#return_stmt.
    def exitReturn_stmt(self, ctx:MicroParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by MicroParser#expr.
    def enterExpr(self, ctx:MicroParser.ExprContext):
        pass

    # Exit a parse tree produced by MicroParser#expr.
    def exitExpr(self, ctx:MicroParser.ExprContext):
        pass


    # Enter a parse tree produced by MicroParser#expr_prefix.
    def enterExpr_prefix(self, ctx:MicroParser.Expr_prefixContext):
        pass

    # Exit a parse tree produced by MicroParser#expr_prefix.
    def exitExpr_prefix(self, ctx:MicroParser.Expr_prefixContext):
        pass


    # Enter a parse tree produced by MicroParser#factor.
    def enterFactor(self, ctx:MicroParser.FactorContext):
        pass

    # Exit a parse tree produced by MicroParser#factor.
    def exitFactor(self, ctx:MicroParser.FactorContext):
        pass


    # Enter a parse tree produced by MicroParser#factor_prefix.
    def enterFactor_prefix(self, ctx:MicroParser.Factor_prefixContext):
        pass

    # Exit a parse tree produced by MicroParser#factor_prefix.
    def exitFactor_prefix(self, ctx:MicroParser.Factor_prefixContext):
        pass


    # Enter a parse tree produced by MicroParser#postfix_expr.
    def enterPostfix_expr(self, ctx:MicroParser.Postfix_exprContext):
        pass

    # Exit a parse tree produced by MicroParser#postfix_expr.
    def exitPostfix_expr(self, ctx:MicroParser.Postfix_exprContext):
        pass


    # Enter a parse tree produced by MicroParser#call_expr.
    def enterCall_expr(self, ctx:MicroParser.Call_exprContext):
        pass

    # Exit a parse tree produced by MicroParser#call_expr.
    def exitCall_expr(self, ctx:MicroParser.Call_exprContext):
        pass


    # Enter a parse tree produced by MicroParser#expr_list.
    def enterExpr_list(self, ctx:MicroParser.Expr_listContext):
        pass

    # Exit a parse tree produced by MicroParser#expr_list.
    def exitExpr_list(self, ctx:MicroParser.Expr_listContext):
        pass


    # Enter a parse tree produced by MicroParser#expr_list_tail.
    def enterExpr_list_tail(self, ctx:MicroParser.Expr_list_tailContext):
        pass

    # Exit a parse tree produced by MicroParser#expr_list_tail.
    def exitExpr_list_tail(self, ctx:MicroParser.Expr_list_tailContext):
        pass


    # Enter a parse tree produced by MicroParser#primary.
    def enterPrimary(self, ctx:MicroParser.PrimaryContext):
        pass

    # Exit a parse tree produced by MicroParser#primary.
    def exitPrimary(self, ctx:MicroParser.PrimaryContext):
        pass


    # Enter a parse tree produced by MicroParser#addop.
    def enterAddop(self, ctx:MicroParser.AddopContext):
        pass

    # Exit a parse tree produced by MicroParser#addop.
    def exitAddop(self, ctx:MicroParser.AddopContext):
        pass


    # Enter a parse tree produced by MicroParser#mulop.
    def enterMulop(self, ctx:MicroParser.MulopContext):
        pass

    # Exit a parse tree produced by MicroParser#mulop.
    def exitMulop(self, ctx:MicroParser.MulopContext):
        pass


    # Enter a parse tree produced by MicroParser#if_stmt.
    def enterIf_stmt(self, ctx:MicroParser.If_stmtContext):
        pass

    # Exit a parse tree produced by MicroParser#if_stmt.
    def exitIf_stmt(self, ctx:MicroParser.If_stmtContext):
        pass


    # Enter a parse tree produced by MicroParser#else_part.
    def enterElse_part(self, ctx:MicroParser.Else_partContext):
        pass

    # Exit a parse tree produced by MicroParser#else_part.
    def exitElse_part(self, ctx:MicroParser.Else_partContext):
        pass


    # Enter a parse tree produced by MicroParser#cond.
    def enterCond(self, ctx:MicroParser.CondContext):
        pass

    # Exit a parse tree produced by MicroParser#cond.
    def exitCond(self, ctx:MicroParser.CondContext):
        pass


    # Enter a parse tree produced by MicroParser#compop.
    def enterCompop(self, ctx:MicroParser.CompopContext):
        pass

    # Exit a parse tree produced by MicroParser#compop.
    def exitCompop(self, ctx:MicroParser.CompopContext):
        pass


    # Enter a parse tree produced by MicroParser#init_stmt.
    def enterInit_stmt(self, ctx:MicroParser.Init_stmtContext):
        pass

    # Exit a parse tree produced by MicroParser#init_stmt.
    def exitInit_stmt(self, ctx:MicroParser.Init_stmtContext):
        pass


    # Enter a parse tree produced by MicroParser#incr_stmt.
    def enterIncr_stmt(self, ctx:MicroParser.Incr_stmtContext):
        pass

    # Exit a parse tree produced by MicroParser#incr_stmt.
    def exitIncr_stmt(self, ctx:MicroParser.Incr_stmtContext):
        pass


    # Enter a parse tree produced by MicroParser#for_stmt.
    def enterFor_stmt(self, ctx:MicroParser.For_stmtContext):
        pass

    # Exit a parse tree produced by MicroParser#for_stmt.
    def exitFor_stmt(self, ctx:MicroParser.For_stmtContext):
        pass


    # Enter a parse tree produced by MicroParser#aug_stmt_list.
    def enterAug_stmt_list(self, ctx:MicroParser.Aug_stmt_listContext):
        pass

    # Exit a parse tree produced by MicroParser#aug_stmt_list.
    def exitAug_stmt_list(self, ctx:MicroParser.Aug_stmt_listContext):
        pass


    # Enter a parse tree produced by MicroParser#aug_stmt.
    def enterAug_stmt(self, ctx:MicroParser.Aug_stmtContext):
        pass

    # Exit a parse tree produced by MicroParser#aug_stmt.
    def exitAug_stmt(self, ctx:MicroParser.Aug_stmtContext):
        pass


    # Enter a parse tree produced by MicroParser#aug_if_stmt.
    def enterAug_if_stmt(self, ctx:MicroParser.Aug_if_stmtContext):
        pass

    # Exit a parse tree produced by MicroParser#aug_if_stmt.
    def exitAug_if_stmt(self, ctx:MicroParser.Aug_if_stmtContext):
        pass


    # Enter a parse tree produced by MicroParser#aug_else_part.
    def enterAug_else_part(self, ctx:MicroParser.Aug_else_partContext):
        pass

    # Exit a parse tree produced by MicroParser#aug_else_part.
    def exitAug_else_part(self, ctx:MicroParser.Aug_else_partContext):
        pass



del MicroParser