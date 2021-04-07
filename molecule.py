# Jonathon Everatt
# Assignment 3, Question 1

# Developing a lexer and parser for Molecules

import ply.lex as lex
import ply.yacc as yacc

global bFlag
bFlag = True
# Lexer code

tokens = [
    'SYMBOL',
    'NUMBER'
]

t_SYMBOL = (
    r"A[lrsgutcm]|B[eraikh]?|C[laroudsemfn]?|D[ybs]|E[urs]|F[erml]?|"
    r"G[aed]|H[eofgs]?|I[nr]?|Kr?|L[iaurv]|M[gnodtc]|N[eiabdpob]?|"
    r"O[sg]?|P[drmtboau]?|R[buhenafg]|S[icernbmg]?|T[icebmalhs]|"
    r"U|V|W|Xe|Yb?|Z[nr]"
)


def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t


t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

# Parser Code
#global count
count = 0


def p_expression_count(p):
    'expression : SYMBOL NUMBER expression'
    global count
    count += p[2]


def p_expression_symbol(p):
    'expression : SYMBOL expression'
    global count
    count += 1


def p_expression_symbcount(p):
    'expression : '
    pass


def p_error(p):
    print("error in formula")
    global bFlag
    bFlag = False


parser = yacc.yacc(debug=False)

if __name__ == "__main__":
    #global count
    #global bFlag
    dataOut = []
    dataIn = ""
    while dataIn != "#":
        dataIn = input()
