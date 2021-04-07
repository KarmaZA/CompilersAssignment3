# Jonathon Everatt
# Assignment 3, Question 1

# Developing a lexer and parser for Molecules

import ply.lex as lex

tokens = [
    'SYMBOL',
    'NUMBER'
]

t_SYMBOL = r'[A-Z][a-z]'
t_NUMBER = r'[0-9_]'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

if __name__ == "__main__":
    check = input()
    data = ""
    while check.find("#") != 0:
        data += check + "\n"
        check = input()
    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok:
            break
        mystr = str(tok)
        if mystr.index("(") > 0:
            mystr = mystr[mystr.index("("):]
            mystr = mystr.replace(",", ", ")
            mystr = mystr[0:1] + "'" + map(mystr[1:mystr.index(",")]) + "'" + mystr[mystr.index(","):]
        print(mystr)
