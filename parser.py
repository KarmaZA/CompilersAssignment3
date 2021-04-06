# Assignment 3 Question 2
# Jonathon Everatt

import ply.yacc as yacc

from lexer import tokens

bFlag = True


def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_expression_equals(p):
    'expression : expression EQUALS term'
    p[0] = p[1] + p[3]


def p_factor_expr(p):  # error is here
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]


def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]


def p_factor_name(p):
    'factor : NAME'
    p[0] = p[1]


def p_error(p):
    # print("Error in input")
    bFlag = False


parser = yacc.yacc()

if __name__ == "__main__":
    check = input()
    data = ""
    while check.find("#") != 0:
        data += check + "\n"
        check = input()
    # print(data)

    result = parser.parse(str(data))
    if bFlag:
        print(result)
    else:
        print("Error in input")
