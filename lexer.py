# Jonathon Everatt Compilers Assignment 3 Question 1
#
# Developing a lexer for a simple adder that could be encountered in a programming language
#
import ply.lex as lex
bf = True

# List of token names
tokens = [
    'NAME',
    'NUMBER',
    'EQUALS',
    'PLUS',
    'LPAREN',
    'RPAREN'
]
# RE rules for simple tokens
t_PLUS = r'\+'
t_EQUALS = r'\='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'


def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except:
        print("Integer value too large %d", t.value)
        t.value = 0

    return t


# Keep track of line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Ignore rule for spaces and tabs
t_ignore = ' \t'


# Rule for illegal characters and errors
def t_error(t):

    if __name__ == "__main__":
        print("Illegal character '%s'" % t.value[0])
    else:
        #print("Error in Input")
        global bf
        bf = False
    t.lexer.skip(1)


def map(data):
    if data == "EQUALS":
        return "="
    elif data == "PLUS":
        return "+"
    elif data == "LPAREN":
        return "("
    elif data == "RPAREN":
        return ")"
    else:
        return data


# build the lexer
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
