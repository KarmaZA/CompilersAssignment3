# Assignment 3 Question 2
# Jonathon Everatt

import ply.yacc as yacc

from lexer import tokens
import lexer

bFlag = True

names = ""
terms = {}


def p_expression_equals(p):
    'expression : NAME EQUALS expression'
    global names, bFlag, terms

    if str(names) == (str(p[1])):
        bFlag = False
    else:
        names = str(p[1])

        if terms and terms["0"] == names:
            bFlag = False
    p[1] = p[3]


def p_expression_plus(p):
    'expression : expression PLUS expression'
    p[0] = str(p[1]) + str(p[3])


def p_expression_paren(p):
    'expression : LPAREN expression RPAREN'
    p[0] = (p[2])


def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]


def p_expression_name(p):
    'expression : NAME'
    p[0] = str(p[1])
    global names, bFlag, terms
    if names == str(p[1]):
        bFlag = False
    elif bool(terms) and terms["0"] != str(p[1]):
        bFlag = False
    else:
        terms["0"] = str(p[1])


def p_error(p):
    # print("Error in input")
    global bFlag
    bFlag = False


parser = yacc.yacc(debug=False)


def run():
    global names,bFlag
    check = input()
    data = ""
    while check.find("#") != 0:
        data += check + "\n"
        parser.parse(str(check))
        if names == "":
            bFlag = False
        names = ""
        check = input()

    if bFlag and lexer.bf:
        print("Accepted")
    else:
        print("Error in input")


if __name__ == "__main__":
    run()
