# Assignment 3 Question 2
# Jonathon Everatt

import ply.yacc as yacc

from lexer import tokens
import lexer
bFlag = True

names = {}


def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]


def p_expression_equals(p):
    'expression : NAME EQUALS expression'
    names[p[1]] = p[3]
    print(names)
    p[1] = p[3]


def p_factor_number(p):
    'factor : NUMBER'
    p[0] = p[1]


def p_factor_name(p):
    'factor : NAME'
    p[0] = p[1]
#    try:
#        p[0] = names[p[1]]
#    except LookupError:
#        global bFlag
#        bFlag = False
#        p[0] = 0


def p_error(p):
    #print("Error in input")
    #print(str(p))
    global bFlag
    bFlag = False


parser = yacc.yacc()#debug=False)
if __name__ == "__main__":
    check = input()
    data = ""
    while check.find("#") != 0:
        data += check + "\n"
        check = input()

    result = parser.parse(str(check))
    if bFlag and lexer.bf:
        print("Accepted")
    else:
        print("Error in input")
