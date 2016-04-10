# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex
from ply.lex import TOKEN

# List of token names.   This is always required
tokens = (
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

digit            = r'([0-9])'
nondigit         = r'([_A-Za-z])'
identifier       = r'(' + nondigit + r'(' + digit + r'|' + nondigit + r')*)' 

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value) 
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Compute column. 
#     input is the input text string
#     token is a token instance
def find_column(input,token):
    last_cr = input.rfind('\n',0,token.lexpos)
    if last_cr < 0:
      last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

@TOKEN(identifier)
def t_ID(t):
    t.value

def t_COMMENT(t):
    r'\#.*'
    pass
    # No return value. Token discarded

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("%d:%d:Illegal character '%s'" % (t.lexer.lineno,find_column(t.lexer.lexdata,t),t.value[0]))
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''(3 + 4) * 10 s 12'''

# Give the lexer some input
#lexer.input(data)


# Tokenize
#for tok in lexer:
#    #print(tok)
#    print(tok.type, tok.value, tok.lineno, tok.lexpos)
