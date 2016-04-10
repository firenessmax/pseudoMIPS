
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '40EAC1AEFFE9FD05CA6A1744A92CB21E'
    
_lr_action_items = {'RPAREN':([1,5,10,11,12,13,14,15,],[-7,11,-1,-6,-2,-5,-3,-4,]),'DIVIDE':([1,3,5,10,11,12,13,14,15,],[-7,7,7,-1,-6,7,-5,7,-4,]),'NUMBER':([0,2,4,6,7,8,9,],[1,1,1,1,1,1,1,]),'TIMES':([1,3,5,10,11,12,13,14,15,],[-7,9,9,-1,-6,9,-5,9,-4,]),'PLUS':([1,3,5,10,11,12,13,14,15,],[-7,6,6,-1,-6,-2,-5,-3,-4,]),'LPAREN':([0,2,4,6,7,8,9,],[2,2,2,2,2,2,2,]),'MINUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,],[4,-7,4,8,4,8,4,4,4,4,-1,-6,-2,-5,-3,-4,]),'$end':([1,3,10,11,12,13,14,15,],[-7,0,-1,-6,-2,-5,-3,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,4,6,7,8,9,],[3,5,10,12,13,14,15,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> MINUS expression','expression',2,'p_expr_uminus','calcparse.py',23),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','calcparse.py',27),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','calcparse.py',28),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','calcparse.py',29),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','calcparse.py',30),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','calcparse.py',36),
  ('expression -> NUMBER','expression',1,'p_expression_number','calcparse.py',40),
]
