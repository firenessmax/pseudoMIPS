# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from calclex import tokens


class Node:
    def __init__(self,type,children=None,leaf=None):
         self.type = type
         if children:
              self.children = children
         else:
              self.children = [ ]
         self.leaf = leaf
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),            # Unary minus operator
)
def p_expr_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = Node("minus-expression",p[2])
    
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''

    p[0] = Node("binop", [p[1],p[3]], p[2])


def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = Node("group-expression",p[2])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = Node("number-expression",p[1])

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")



class posorden:
  indicador=0
  def recorrido(self,nodo):
    if nodo is None:
      return
    if(nodo.type=="binop"):
      self.recorrido(nodo.children[0])
      self.recorrido(nodo.children[1])
      if nodo.leaf=='+':
        print "add $t%d,$t%d,$t%d"%(self.indicador-2,self.indicador-2,self.indicador-1)
      elif nodo.leaf=='*':
        print "mul $t%d,$t%d,$t%d"%(self.indicador-2,self.indicador-2,self.indicador-1)
      if nodo.leaf=='-':
        print "sub $t%d,$t%d,$t%d"%(self.indicador-2,self.indicador-2,self.indicador-1)
      elif nodo.leaf=='/':
        print "div $t%d,$t%d,$t%d"%(self.indicador-2,self.indicador-2,self.indicador-1)
      self.indicador-=1
    elif nodo.type=="group-expression":
      self.recorrido(nodo.children)
    elif nodo.type=="minus-expression":
      print "sub $t%d,$zero,$t%d"%(self.indicador,self.indicador-1)
      self.indicador+=1
    else:
      print "addi $t%d, $zero,%d"%(self.indicador,nodo.children)
      self.indicador+=1

  


# Build the parser
parser = yacc.yacc()


while True:
  try:
    s = raw_input('calc > ')
  except EOFError:
    break
  if not s: continue
  nodes = parser.parse(s)
  p=posorden()
  p.recorrido(nodes)
12+12*(3/12)