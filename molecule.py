# Jonathon Everatt
# Assignment 3, Question 1

# Developing a lexer and parser for Molecules

import ply.lex as lex
import ply.yacc as yacc

global lastEle
lastEle = ""

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
    # print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    global bFlag
    bFlag = False


lexer = lex.lex()

# Parser Code
# global count
count = 0


def p_expression_count(p):
    'expression : SYMBOL NUMBER expression'
    global count
    count += p[2]
    global lastEle
    lastEle = ""


def p_expression_symbol(p):
    'expression : SYMBOL expression'
    global count
    count += 1
    global lastEle
    if lastEle == str(p[1]):
        global bFlag
        bFlag = False
    else:
        lastEle = str(p[1])


def p_expression_symbcount(p):
    'expression : '
    pass


def p_error(p):
    #print("Error in formula")
    global bFlag
    bFlag = False


parser = yacc.yacc(debug=False)


# has to be in a method or global count throws errors
def run():
    global count
    global bFlag
    dataOut = []
    dataIn = input()
    while dataIn != "#":
        dataOut.append(dataIn)
        dataIn = input()
   #print(dataOut)

    for inputs in dataOut:
        count = 0
        parser.parse(inputs)

        if bFlag:
            print(count)
        else:
            print("Error in formula")
        bFlag = True


if __name__ == "__main__":
    run()
