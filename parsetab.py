
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'IDENTIFIER NON_STRICT_COMPARISON NON_EQUALITY COMPARISON ASSIGNMENT SEMICOLON EQUALITY COLON OPEN_BRACKET CLOSE_BRACKET OPEN_SQUARE_BRACKET CLOSE_SQUARE_BRACKET NUMBER PLUS MINUS DIV MUL STRING POINT ZAPYATAYA AND THEN IN TYPE_INTEGER IF WRITELN END FOR DOWNTO WHILE WRITE TO VAR INC TYPE_REAL DO BEGIN TYPE_STRING READ ELSE BREAK NOT CONST READLN LENGTH OR\n        consts : CONST IDENTIFIER EQUALITY NUMBER SEMICOLON begin_program\n                | CONST IDENTIFIER EQUALITY STRING SEMICOLON begin_program\n                | CONST IDENTIFIER EQUALITY matrix SEMICOLON begin_program\n                | begin_program\n    \n        matrix : OPEN_SQUARE_BRACKET identifiers CLOSE_SQUARE_BRACKET\n    \n        identifiers : IDENTIFIER ZAPYATAYA identifiers\n                    | NUMBER ZAPYATAYA identifiers\n                    | STRING ZAPYATAYA identifiers\n                    | IDENTIFIER\n                    | NUMBER\n                    | STRING\n    \n        begin_program : VAR declarations BEGIN body END POINT\n    \n        block : BEGIN body END SEMICOLON\n    \n        body : expression\n    \n        identifier : IDENTIFIER\n                    | IDENTIFIER SEMICOLON\n    \n    expression : assignment expression\n                | if expression\n                | function expression\n                | empty\n                | while expression\n                | for expression\n                | break\n    \n        break : BREAK SEMICOLON\n    \n        declarations : declaration declarations\n                    | empty\n    \n        declaration : IDENTIFIER another_identifiers COLON type SEMICOLON\n    \n        another_identifiers : ZAPYATAYA IDENTIFIER another_identifiers\n                            | empty\n    \n        type : TYPE_STRING\n             | TYPE_INTEGER\n             | TYPE_REAL\n    \n        empty :\n    \n        assignment : identifier ASSIGNMENT arithmetic_expression SEMICOLON\n                   | identifier ASSIGNMENT function SEMICOLON\n                   | identifier ASSIGNMENT function\n                   | identifier ASSIGNMENT arithmetic_expression\n    \n    arithmetic_expression : NUMBER\n                     | identifier\n                     | STRING\n                     | function\n                     | identifier PLUS arithmetic_expression\n                     | identifier MINUS arithmetic_expression\n                     | identifier MUL arithmetic_expression\n                     | identifier DIV arithmetic_expression\n                     | NUMBER PLUS arithmetic_expression\n                     | NUMBER MINUS arithmetic_expression\n                     | NUMBER MUL arithmetic_expression\n                     | NUMBER DIV arithmetic_expression\n                     | function PLUS arithmetic_expression\n                     | function MINUS arithmetic_expression\n                     | function MUL arithmetic_expression\n                     | function DIV arithmetic_expression\n                     | identifier OPEN_SQUARE_BRACKET arithmetic_expression CLOSE_SQUARE_BRACKET\n                     | arithmetic_expression PLUS arithmetic_expression\n                     | arithmetic_expression MINUS arithmetic_expression\n                     | arithmetic_expression MUL arithmetic_expression\n                     | arithmetic_expression DIV arithmetic_expression\n                     | arithmetic_expression SEMICOLON\n    \n        function : WRITE OPEN_BRACKET arithmetic_expression CLOSE_BRACKET SEMICOLON\n                    | WRITELN OPEN_BRACKET arithmetic_expression CLOSE_BRACKET SEMICOLON\n                    | READ OPEN_BRACKET identifier CLOSE_BRACKET SEMICOLON\n                    | READLN OPEN_BRACKET identifier CLOSE_BRACKET SEMICOLON\n                    | LENGTH OPEN_BRACKET identifier CLOSE_BRACKET\n                    | INC OPEN_BRACKET identifier CLOSE_BRACKET SEMICOLON\n                    | LENGTH OPEN_BRACKET identifier CLOSE_BRACKET SEMICOLON\n    \n    predicate :    arithmetic_expression COMPARISON arithmetic_expression\n                  | arithmetic_expression EQUALITY arithmetic_expression\n                  | arithmetic_expression NON_EQUALITY arithmetic_expression\n                  | arithmetic_expression NON_STRICT_COMPARISON arithmetic_expression\n                  | arithmetic_expression IN identifier\n                  | arithmetic_expression IN matrix\n    \n        some_predicates : OPEN_BRACKET predicate CLOSE_BRACKET AND some_predicates\n                        | OPEN_BRACKET predicate CLOSE_BRACKET OR some_predicates\n                        | OPEN_BRACKET predicate CLOSE_BRACKET\n                        | OPEN_BRACKET NOT OPEN_BRACKET predicate CLOSE_BRACKET CLOSE_BRACKET AND some_predicates\n                        | OPEN_BRACKET NOT OPEN_BRACKET predicate CLOSE_BRACKET CLOSE_BRACKET OR some_predicates\n                        | OPEN_BRACKET NOT OPEN_BRACKET predicate CLOSE_BRACKET CLOSE_BRACKET\n    \n        while : WHILE OPEN_BRACKET predicate CLOSE_BRACKET DO block\n              | WHILE some_predicates DO block\n    \n        for : FOR assignment TO arithmetic_expression DO block\n              | FOR assignment DOWNTO arithmetic_expression DO block\n    \n        if : IF OPEN_BRACKET predicate CLOSE_BRACKET THEN block\n            | IF OPEN_BRACKET predicate CLOSE_BRACKET THEN block else\n    \n        else : ELSE block\n    '
    
_lr_action_items = {'CLOSE_BRACKET':([22,50,74,75,76,77,78,81,83,87,88,89,90,93,98,113,133,143,144,145,146,147,148,149,150,151,155,156,157,158,159,160,161,162,163,164,165,167,168,169,170,172,175,177,178,179,184,185,190,],[-15,-16,102,-38,-41,111,-40,-39,130,133,134,135,136,139,-5,-59,-64,-62,-46,-48,-49,-47,-50,-52,-53,-51,-67,-69,-70,-57,-55,-71,-72,-68,-58,-56,184,-42,-44,-45,-43,-61,-66,-60,-63,-65,191,-54,195,]),'ZAPYATAYA':([7,37,69,71,72,],[12,12,97,99,100,]),'TYPE_STRING':([38,],[63,]),'CONST':([0,],[4,]),'DO':([22,46,50,75,76,78,81,111,113,131,132,133,143,144,145,146,147,148,149,150,151,158,159,163,164,167,168,169,170,172,175,177,178,179,181,183,185,191,195,199,200,],[-15,82,-16,-38,-41,-40,-39,152,-59,173,174,-64,-62,-46,-48,-49,-47,-50,-52,-53,-51,-57,-55,-58,-56,-42,-44,-45,-43,-61,-66,-60,-63,-65,-74,-73,-54,-78,-75,-76,-77,]),'READ':([10,16,20,22,26,31,33,45,47,50,55,56,60,75,76,78,81,85,86,91,92,103,104,105,106,107,108,109,110,112,113,114,115,116,117,119,120,121,122,123,124,125,126,127,128,129,133,137,138,143,144,145,146,147,148,149,150,151,158,159,163,164,167,168,169,170,172,175,177,178,179,180,182,185,187,188,189,192,193,198,],[17,17,17,-15,17,17,17,17,17,-16,17,17,17,-38,-41,-40,-39,17,17,-36,-37,17,17,17,17,17,17,17,17,17,-59,17,17,17,17,17,17,17,17,17,17,17,17,17,17,-80,-64,-35,-34,-62,-46,-48,-49,-47,-50,-52,-53,-51,-57,-55,-58,-56,-42,-44,-45,-43,-61,-66,-60,-63,-65,-79,17,-54,-82,-81,-83,-13,-84,-85,]),'ASSIGNMENT':([22,34,50,],[-15,60,-16,]),'TYPE_INTEGER':([38,],[65,]),'THEN':([134,],[176,]),'NUMBER':([15,41,45,47,55,56,60,85,86,97,99,100,103,104,105,106,107,108,109,110,112,114,115,116,117,119,120,121,122,123,124,125,126,127,182,],[40,71,75,75,75,75,75,75,75,71,71,71,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,]),'WHILE':([10,16,20,22,26,31,33,50,75,76,78,81,91,92,113,128,129,133,137,138,143,144,145,146,147,148,149,150,151,158,159,163,164,167,168,169,170,172,175,177,178,179,180,185,187,188,189,192,193,198,],[18,18,18,-15,18,18,18,-16,-38,-41,-40,-39,-36,-37,-59,18,-80,-64,-35,-34,-62,-46,-48,-49,-47,-50,-52,-53,-51,-57,-55,-58,-56,-42,-44,-45,-43,-61,-66,-60,-63,-65,-79,-54,-82,-81,-83,-13,-84,-85,]),'OPEN_SQUARE_BRACKET':([15,22,50,81,118,],[41,-15,-16,123,41,]),'MUL':([22,50,75,76,78,79,81,83,89,91,92,113,131,132,133,138,143,144,145,146,147,148,149,150,151,155,156,157,158,159,162,163,164,166,167,168,169,170,172,175,177,178,179,185,],[-15,-16,104,108,-40,116,125,116,116,108,116,-59,116,116,-64,-59,-62,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,-61,-66,-60,-63,-65,-54,]),'NON_STRICT_COMPARISON':([22,50,75,76,78,79,81,113,133,143,144,145,146,147,148,149,150,151,158,159,163,164,167,168,169,170,172,175,177,178,179,185,],[-15,-16,-38,-41,-40,115,-39,-59,-64,-62,-46,-48,-49,-47,-50,-52,-53,-51,-57,-55,-58,-56,-42,-44,-45,-43,-61,-66,-60,-63,-65,-54,]),'DIV':([22,50,75,76,78,79,81,83,89,91,92,113,131,132,133,138,143,144,145,146,147,148,149,150,151,155,156,157,158,159,162,163,164,166,167,168,169,170,172,175,177,178,179,185,],[-15,-16,105,109,-40,120,126,120,120,109,120,-59,120,120,-64,-59,-62,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,-61,-66,-60,-63,-65,-54,]),'MINUS':([22,50,75,76,78,79,81,83,89,91,92,113,131,132,133,138,143,144,145,146,147,148,149,150,151,155,156,157,158,159,162,163,164,166,167,168,169,170,172,175,177,178,179,185,],[-15,-16,106,110,-40,121,127,121,121,110,121,-59,121,121,-64,-59,-62,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,-61,-66,-60,-63,-65,-54,]),'BREAK':([10,16,20,22,26,31,33,50,75,76,78,81,91,92,113,128,129,133,137,138,143,144,145,146,147,148,149,150,151,158,159,163,164,167,168,169,170,172,175,177,178,179,180,185,187,188,189,192,193,198,],[21,21,21,-15,21,21,21,-16,-38,-41,-40,-39,-36,-37,-59,21,-80,-64,-35,-34,-62,-46,-48,-49,-47,-50,-52,-53,-51,-57,-55,-58,-56,-42,-44,-45,-43,-61,-66,-60,-63,-65,-79,-54,-82,-81,-83,-13,-84,-85,]),'BEGIN':([3,5,6,8,11,82,94,152,173,174,176,194,],[-33,10,-33,-26,-25,128,-27,128,128,128,128,128,]),'EQUALITY':([9,22,50,75,76,78,79,81,113,133,143,144,145,146,147,148,149,150,151,158,159,163,164,167,168,169,170,172,175,177,178,179,185,],[15,-15,-16,-38,-41,-40,119,-39,-59,-64,-62,-46,-48,-49,-47,-50,-52,-53,-51,-57,-55,-58,-56,-42,-44,-45,-43,-61,-66,-60,-63,-65,-54,]),'SEMICOLON':([21,22,39,40,42,50,63,64,65,66,75,76,78,79,81,83,89,91,92,98,102,113,130,131,132,133,135,136,138,139,143,144,145,146,147,148,149,150,151,155,156,157,158,159,162,163,164,166,167,168,169,170,172,175,177,178,179,185,186,],[49,50,67,68,73,-16,-30,-32,-31,94,-38,-41,-40,113,-39,113,113,137,138,-5,143,-59,172,113,113,175,177,178,-59,179,-62,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,-61,-66,-60,-63,-65,-54,192,]),'POINT':([51,],[84,]),'CLOSE_SQUARE_BRACKET':([22,50,69,70,71,72,75,76,78,81,113,133,140,141,142,143,144,145,146,147,148,149,150,151,158,159,163,164,166,167,168,169,170,172,175,177,178,179,185,],[-15,-16,-11,98,-10,-9,-38,-41,-40,-39,-59,-64,-8,-7,-6,-62,-46,-48,-49,-47,-50,-52,-53,-51,-57,-55,-58,-56,185,-42,-44,-45,-43,-61,-66,-60,-63,-65,-54,]),'OPEN_BRACKET':([17,18,19,28,29,30,32,36,80,153,154,196,197,],[44,45,47,54,55,56,58,61,122,182,182,182,182,]),'TO':([22,50,52,75,76,78,81,91,92,113,133,137,138,143,144,145,146,147,148,149,150,151,158,159,163,164,167,168,169,170,172,175,177,178,179,185,],[-15,-16,86,-38,-41,-40,-39,-36,-37,-59,-64,-35,-34,-62,-46,-48,-49,-47,-50,-52,-53,-51,-57,-55,-58,-56,-42,-44,-45,-43,-61,-66,-60,-63,-65,-54,]),'COLON':([7,13,14,37,62,],[-33,38,-29,-33,-28,]),'PLUS':([22,50,75,76,78,79,81,83,89,91,92,113,131,132,133,138,143,144,145,146,147,148,149,150,151,155,156,157,158,159,162,163,164,166,167,168,169,170,172,175,177,178,179,185,],[-15,-16,103,107,-40,117,124,117,117,107,117,-59,117,117,-64,-59,-62,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,-61,-66,-60,-63,-65,-54,]),'IDENTIFIER':([3,4,6,10,12,16,20,22,25,26,31,33,41,44,45,47,50,54,55,56,58,60,61,75,76,78,81,85,86,91,92,94,97,99,100,103,104,105,106,107,108,109,110,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,133,137,138,143,144,145,146,147,148,149,150,151,158,159,163,164,167,168,169,170,172,175,177,178,179,180,182,185,187,188,189,192,193,198,],[7,9,7,22,37,22,22,-15,22,22,22,22,72,22,22,22,-16,22,22,22,22,22,22,-38,-41,-40,-39,22,22,-36,-37,-27,72,72,72,22,22,22,22,22,22,22,22,22,-59,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,-80,-64,-35,-34,-62,-46,-48,-49,-47,-50,-52,-53,-51,-57,-55,-58,-56,-42,-44,-45,-43,-61,-66,-60,-63,-65,-79,22,-54,-82,-81,-83,-13,-84,-85,]),'$end':([1,2,84,95,96,101,],[-4,0,-12,-2,-1,-3,]),'END':([10,16,20,22,23,24,26,27,31,33,35,43,48,49,50,53,57,59,75,76,78,81,91,92,113,128,129,133,137,138,143,144,145,146,147,148,149,150,151,158,159,163,164,167,168,169,170,171,172,175,177,178,179,180,185,187,188,189,192,193,198,],[-33,-33,-33,-15,-20,51,-33,-23,-33,-33,-14,-19,-18,-24,-16,-17,-22,-21,-38,-41,-40,-39,-36,-37,-59,-33,-80,-64,-35,-34,-62,-46,-48,-49,-47,-50,-52,-53,-51,-57,-55,-58,-56,-42,-44,-45,-43,186,-61,-66,-60,-63,-65,-79,-54,-82,-81,-83,-13,-84,-85,]),'STRING':([15,41,45,47,55,56,60,85,86,97,99,100,103,104,105,106,107,108,109,110,112,114,115,116,117,119,120,121,122,123,124,125,126,127,182,],[39,69,78,78,78,78,78,78,78,69,69,69,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,]),'FOR':([10,16,20,22,26,31,33,50,75,76,78,81,91,92,113,128,129,133,137,138,143,144,145,146,147,148,149,150,151,158,159,163,164,167,168,169,170,172,175,177,178,179,180,185,187,188,189,192,193,198,],[25,25,25,-15,25,25,25,-16,-38,-41,-40,-39,-36,-37,-59,25,-80,-64,-35,-34,-62,-46,-48,-49,-47,-50,-52,-53,-51,-57,-55,-58,-56,-42,-44,-45,-43,-61,-66,-60,-63,-65,-79,-54,-82,-81,-83,-13,-84,-85,]),'COMPARISON':([22,50,75,76,78,79,81,113,133,143,144,145,146,147,148,149,150,151,158,159,163,164,167,168,169,170,172,175,177,178,179,185,],[-15,-16,-38,-41,-40,112,-39,-59,-64,-62,-46,-48,-49,-47,-50,-52,-53,-51,-57,-55,-58,-56,-42,-44,-45,-43,-61,-66,-60,-63,-65,-54,]),'ELSE':([189,192,],[194,-13,]),'WRITE':([10,16,20,22,26,31,33,45,47,50,55,56,60,75,76,78,81,85,86,91,92,103,104,105,106,107,108,109,110,112,113,114,115,116,117,119,120,121,122,123,124,125,126,127,128,129,133,137,138,143,144,145,146,147,148,149,150,151,158,159,163,164,167,168,169,170,172,175,177,178,179,180,182,185,187,188,189,192,193,198,],[30,30,30,-15,30,30,30,30,30,-16,30,30,30,-38,-41,-40,-39,30,30,-36,-37,30,30,30,30,30,30,30,30,30,-59,30,30,30,30,30,30,30,30,30,30,30,30,30,30,-80,-64,-35,-34,-62,-46,-48,-49,-47,-50,-52,-53,-51,-57,-55,-58,-56,-42,-44,-45,-43,-61,-66,-60,-63,-65,-79,30,-54,-82,-81,-83,-13,-84,-85,]),'IN':([22,50,75,76,78,79,81,113,133,143,144,145,146,147,148,149,150,151,158,159,163,164,167,168,169,170,172,175,177,178,179,185,],[-15,-16,-38,-41,-40,118,-39,-59,-64,-62,-46,-48,-49,-47,-50,-52,-53,-51,-57,-55,-58,-56,-42,-44,-45,-43,-61,-66,-60,-63,-65,-54,]),'VAR':([0,67,68,73,],[3,3,3,3,]),'NON_EQUALITY':([22,50,75,76,78,79,81,113,133,143,144,145,146,147,148,149,150,151,158,159,163,164,167,168,169,170,172,175,177,178,179,185,],[-15,-16,-38,-41,-40,114,-39,-59,-64,-62,-46,-48,-49,-47,-50,-52,-53,-51,-57,-55,-58,-56,-42,-44,-45,-43,-61,-66,-60,-63,-65,-54,]),'IF':([10,16,20,22,26,31,33,50,75,76,78,81,91,92,113,128,129,133,137,138,143,144,145,146,147,148,149,150,151,158,159,163,164,167,168,169,170,172,175,177,178,179,180,185,187,188,189,192,193,198,],[29,29,29,-15,29,29,29,-16,-38,-41,-40,-39,-36,-37,-59,29,-80,-64,-35,-34,-62,-46,-48,-49,-47,-50,-52,-53,-51,-57,-55,-58,-56,-42,-44,-45,-43,-61,-66,-60,-63,-65,-79,-54,-82,-81,-83,-13,-84,-85,]),'AND':([111,191,195,],[154,196,154,]),'WRITELN':([10,16,20,22,26,31,33,45,47,50,55,56,60,75,76,78,81,85,86,91,92,103,104,105,106,107,108,109,110,112,113,114,115,116,117,119,120,121,122,123,124,125,126,127,128,129,133,137,138,143,144,145,146,147,148,149,150,151,158,159,163,164,167,168,169,170,172,175,177,178,179,180,182,185,187,188,189,192,193,198,],[19,19,19,-15,19,19,19,19,19,-16,19,19,19,-38,-41,-40,-39,19,19,-36,-37,19,19,19,19,19,19,19,19,19,-59,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-80,-64,-35,-34,-62,-46,-48,-49,-47,-50,-52,-53,-51,-57,-55,-58,-56,-42,-44,-45,-43,-61,-66,-60,-63,-65,-79,19,-54,-82,-81,-83,-13,-84,-85,]),'TYPE_REAL':([38,],[64,]),'READLN':([10,16,20,22,26,31,33,45,47,50,55,56,60,75,76,78,81,85,86,91,92,103,104,105,106,107,108,109,110,112,113,114,115,116,117,119,120,121,122,123,124,125,126,127,128,129,133,137,138,143,144,145,146,147,148,149,150,151,158,159,163,164,167,168,169,170,172,175,177,178,179,180,182,185,187,188,189,192,193,198,],[32,32,32,-15,32,32,32,32,32,-16,32,32,32,-38,-41,-40,-39,32,32,-36,-37,32,32,32,32,32,32,32,32,32,-59,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-80,-64,-35,-34,-62,-46,-48,-49,-47,-50,-52,-53,-51,-57,-55,-58,-56,-42,-44,-45,-43,-61,-66,-60,-63,-65,-79,32,-54,-82,-81,-83,-13,-84,-85,]),'DOWNTO':([22,50,52,75,76,78,81,91,92,113,133,137,138,143,144,145,146,147,148,149,150,151,158,159,163,164,167,168,169,170,172,175,177,178,179,185,],[-15,-16,85,-38,-41,-40,-39,-36,-37,-59,-64,-35,-34,-62,-46,-48,-49,-47,-50,-52,-53,-51,-57,-55,-58,-56,-42,-44,-45,-43,-61,-66,-60,-63,-65,-54,]),'LENGTH':([10,16,20,22,26,31,33,45,47,50,55,56,60,75,76,78,81,85,86,91,92,103,104,105,106,107,108,109,110,112,113,114,115,116,117,119,120,121,122,123,124,125,126,127,128,129,133,137,138,143,144,145,146,147,148,149,150,151,158,159,163,164,167,168,169,170,172,175,177,178,179,180,182,185,187,188,189,192,193,198,],[28,28,28,-15,28,28,28,28,28,-16,28,28,28,-38,-41,-40,-39,28,28,-36,-37,28,28,28,28,28,28,28,28,28,-59,28,28,28,28,28,28,28,28,28,28,28,28,28,28,-80,-64,-35,-34,-62,-46,-48,-49,-47,-50,-52,-53,-51,-57,-55,-58,-56,-42,-44,-45,-43,-61,-66,-60,-63,-65,-79,28,-54,-82,-81,-83,-13,-84,-85,]),'NOT':([45,182,],[80,80,]),'OR':([111,191,195,],[153,197,153,]),'INC':([10,16,20,22,26,31,33,45,47,50,55,56,60,75,76,78,81,85,86,91,92,103,104,105,106,107,108,109,110,112,113,114,115,116,117,119,120,121,122,123,124,125,126,127,128,129,133,137,138,143,144,145,146,147,148,149,150,151,158,159,163,164,167,168,169,170,172,175,177,178,179,180,182,185,187,188,189,192,193,198,],[36,36,36,-15,36,36,36,36,36,-16,36,36,36,-38,-41,-40,-39,36,36,-36,-37,36,36,36,36,36,36,36,36,36,-59,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-80,-64,-35,-34,-62,-46,-48,-49,-47,-50,-52,-53,-51,-57,-55,-58,-56,-42,-44,-45,-43,-61,-66,-60,-63,-65,-79,36,-54,-82,-81,-83,-13,-84,-85,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'function':([10,16,20,26,31,33,45,47,55,56,60,85,86,103,104,105,106,107,108,109,110,112,114,115,116,117,119,120,121,122,123,124,125,126,127,128,182,],[16,16,16,16,16,16,76,76,76,76,91,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,16,76,]),'identifiers':([41,97,99,100,],[70,140,141,142,]),'predicate':([45,55,122,182,],[77,88,165,190,]),'if':([10,16,20,26,31,33,128,],[20,20,20,20,20,20,20,]),'matrix':([15,118,],[42,161,]),'for':([10,16,20,26,31,33,128,],[31,31,31,31,31,31,31,]),'type':([38,],[66,]),'empty':([3,6,7,10,16,20,26,31,33,37,128,],[8,8,14,23,23,23,23,23,23,14,23,]),'body':([10,128,],[24,171,]),'some_predicates':([18,153,154,196,197,],[46,181,183,199,200,]),'begin_program':([0,67,68,73,],[1,95,96,101,]),'assignment':([10,16,20,25,26,31,33,128,],[26,26,26,52,26,26,26,26,]),'else':([189,],[193,]),'break':([10,16,20,26,31,33,128,],[27,27,27,27,27,27,27,]),'consts':([0,],[2,]),'declaration':([3,6,],[6,6,]),'arithmetic_expression':([45,47,55,56,60,85,86,103,104,105,106,107,108,109,110,112,114,115,116,117,119,120,121,122,123,124,125,126,127,182,],[79,83,79,89,92,131,132,144,145,146,147,148,149,150,151,155,156,157,158,159,162,163,164,79,166,167,168,169,170,79,]),'declarations':([3,6,],[5,11,]),'while':([10,16,20,26,31,33,128,],[33,33,33,33,33,33,33,]),'another_identifiers':([7,37,],[13,62,]),'identifier':([10,16,20,25,26,31,33,44,45,47,54,55,56,58,60,61,85,86,103,104,105,106,107,108,109,110,112,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,182,],[34,34,34,34,34,34,34,74,81,81,87,81,81,90,81,93,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,160,81,81,81,81,81,81,81,81,81,34,81,]),'expression':([10,16,20,26,31,33,128,],[35,43,48,53,57,59,35,]),'block':([82,152,173,174,176,194,],[129,180,187,188,189,198,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> consts","S'",1,None,None,None),
  ('consts -> CONST IDENTIFIER EQUALITY NUMBER SEMICOLON begin_program','consts',6,'p_consts','semantic.py',146),
  ('consts -> CONST IDENTIFIER EQUALITY STRING SEMICOLON begin_program','consts',6,'p_consts','semantic.py',147),
  ('consts -> CONST IDENTIFIER EQUALITY matrix SEMICOLON begin_program','consts',6,'p_consts','semantic.py',148),
  ('consts -> begin_program','consts',1,'p_consts','semantic.py',149),
  ('matrix -> OPEN_SQUARE_BRACKET identifiers CLOSE_SQUARE_BRACKET','matrix',3,'p_matrix','semantic.py',159),
  ('identifiers -> IDENTIFIER ZAPYATAYA identifiers','identifiers',3,'p_identifiers','semantic.py',166),
  ('identifiers -> NUMBER ZAPYATAYA identifiers','identifiers',3,'p_identifiers','semantic.py',167),
  ('identifiers -> STRING ZAPYATAYA identifiers','identifiers',3,'p_identifiers','semantic.py',168),
  ('identifiers -> IDENTIFIER','identifiers',1,'p_identifiers','semantic.py',169),
  ('identifiers -> NUMBER','identifiers',1,'p_identifiers','semantic.py',170),
  ('identifiers -> STRING','identifiers',1,'p_identifiers','semantic.py',171),
  ('begin_program -> VAR declarations BEGIN body END POINT','begin_program',6,'p_begin_program','semantic.py',181),
  ('block -> BEGIN body END SEMICOLON','block',4,'p_block','semantic.py',188),
  ('body -> expression','body',1,'p_body','semantic.py',195),
  ('identifier -> IDENTIFIER','identifier',1,'p_identifier','semantic.py',202),
  ('identifier -> IDENTIFIER SEMICOLON','identifier',2,'p_identifier','semantic.py',203),
  ('expression -> assignment expression','expression',2,'p_expression','semantic.py',215),
  ('expression -> if expression','expression',2,'p_expression','semantic.py',216),
  ('expression -> function expression','expression',2,'p_expression','semantic.py',217),
  ('expression -> empty','expression',1,'p_expression','semantic.py',218),
  ('expression -> while expression','expression',2,'p_expression','semantic.py',219),
  ('expression -> for expression','expression',2,'p_expression','semantic.py',220),
  ('expression -> break','expression',1,'p_expression','semantic.py',221),
  ('break -> BREAK SEMICOLON','break',2,'p_break','semantic.py',232),
  ('declarations -> declaration declarations','declarations',2,'p_declarations','semantic.py',239),
  ('declarations -> empty','declarations',1,'p_declarations','semantic.py',240),
  ('declaration -> IDENTIFIER another_identifiers COLON type SEMICOLON','declaration',5,'p_declaration','semantic.py',250),
  ('another_identifiers -> ZAPYATAYA IDENTIFIER another_identifiers','another_identifiers',3,'p_another_identifiers','semantic.py',262),
  ('another_identifiers -> empty','another_identifiers',1,'p_another_identifiers','semantic.py',263),
  ('type -> TYPE_STRING','type',1,'p_type','semantic.py',276),
  ('type -> TYPE_INTEGER','type',1,'p_type','semantic.py',277),
  ('type -> TYPE_REAL','type',1,'p_type','semantic.py',278),
  ('empty -> <empty>','empty',0,'p_empty','semantic.py',285),
  ('assignment -> identifier ASSIGNMENT arithmetic_expression SEMICOLON','assignment',4,'p_assignment','semantic.py',292),
  ('assignment -> identifier ASSIGNMENT function SEMICOLON','assignment',4,'p_assignment','semantic.py',293),
  ('assignment -> identifier ASSIGNMENT function','assignment',3,'p_assignment','semantic.py',294),
  ('assignment -> identifier ASSIGNMENT arithmetic_expression','assignment',3,'p_assignment','semantic.py',295),
  ('arithmetic_expression -> NUMBER','arithmetic_expression',1,'p_arithmetic_expression','semantic.py',305),
  ('arithmetic_expression -> identifier','arithmetic_expression',1,'p_arithmetic_expression','semantic.py',306),
  ('arithmetic_expression -> STRING','arithmetic_expression',1,'p_arithmetic_expression','semantic.py',307),
  ('arithmetic_expression -> function','arithmetic_expression',1,'p_arithmetic_expression','semantic.py',308),
  ('arithmetic_expression -> identifier PLUS arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','semantic.py',309),
  ('arithmetic_expression -> identifier MINUS arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','semantic.py',310),
  ('arithmetic_expression -> identifier MUL arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','semantic.py',311),
  ('arithmetic_expression -> identifier DIV arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','semantic.py',312),
  ('arithmetic_expression -> NUMBER PLUS arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','semantic.py',313),
  ('arithmetic_expression -> NUMBER MINUS arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','semantic.py',314),
  ('arithmetic_expression -> NUMBER MUL arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','semantic.py',315),
  ('arithmetic_expression -> NUMBER DIV arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','semantic.py',316),
  ('arithmetic_expression -> function PLUS arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','semantic.py',317),
  ('arithmetic_expression -> function MINUS arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','semantic.py',318),
  ('arithmetic_expression -> function MUL arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','semantic.py',319),
  ('arithmetic_expression -> function DIV arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','semantic.py',320),
  ('arithmetic_expression -> identifier OPEN_SQUARE_BRACKET arithmetic_expression CLOSE_SQUARE_BRACKET','arithmetic_expression',4,'p_arithmetic_expression','semantic.py',321),
  ('arithmetic_expression -> arithmetic_expression PLUS arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','semantic.py',322),
  ('arithmetic_expression -> arithmetic_expression MINUS arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','semantic.py',323),
  ('arithmetic_expression -> arithmetic_expression MUL arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','semantic.py',324),
  ('arithmetic_expression -> arithmetic_expression DIV arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','semantic.py',325),
  ('arithmetic_expression -> arithmetic_expression SEMICOLON','arithmetic_expression',2,'p_arithmetic_expression','semantic.py',326),
  ('function -> WRITE OPEN_BRACKET arithmetic_expression CLOSE_BRACKET SEMICOLON','function',5,'p_function','semantic.py',369),
  ('function -> WRITELN OPEN_BRACKET arithmetic_expression CLOSE_BRACKET SEMICOLON','function',5,'p_function','semantic.py',370),
  ('function -> READ OPEN_BRACKET identifier CLOSE_BRACKET SEMICOLON','function',5,'p_function','semantic.py',371),
  ('function -> READLN OPEN_BRACKET identifier CLOSE_BRACKET SEMICOLON','function',5,'p_function','semantic.py',372),
  ('function -> LENGTH OPEN_BRACKET identifier CLOSE_BRACKET','function',4,'p_function','semantic.py',373),
  ('function -> INC OPEN_BRACKET identifier CLOSE_BRACKET SEMICOLON','function',5,'p_function','semantic.py',374),
  ('function -> LENGTH OPEN_BRACKET identifier CLOSE_BRACKET SEMICOLON','function',5,'p_function','semantic.py',375),
  ('predicate -> arithmetic_expression COMPARISON arithmetic_expression','predicate',3,'p_predicate','semantic.py',397),
  ('predicate -> arithmetic_expression EQUALITY arithmetic_expression','predicate',3,'p_predicate','semantic.py',398),
  ('predicate -> arithmetic_expression NON_EQUALITY arithmetic_expression','predicate',3,'p_predicate','semantic.py',399),
  ('predicate -> arithmetic_expression NON_STRICT_COMPARISON arithmetic_expression','predicate',3,'p_predicate','semantic.py',400),
  ('predicate -> arithmetic_expression IN identifier','predicate',3,'p_predicate','semantic.py',401),
  ('predicate -> arithmetic_expression IN matrix','predicate',3,'p_predicate','semantic.py',402),
  ('some_predicates -> OPEN_BRACKET predicate CLOSE_BRACKET AND some_predicates','some_predicates',5,'p_some_predicates','semantic.py',457),
  ('some_predicates -> OPEN_BRACKET predicate CLOSE_BRACKET OR some_predicates','some_predicates',5,'p_some_predicates','semantic.py',458),
  ('some_predicates -> OPEN_BRACKET predicate CLOSE_BRACKET','some_predicates',3,'p_some_predicates','semantic.py',459),
  ('some_predicates -> OPEN_BRACKET NOT OPEN_BRACKET predicate CLOSE_BRACKET CLOSE_BRACKET AND some_predicates','some_predicates',8,'p_some_predicates','semantic.py',460),
  ('some_predicates -> OPEN_BRACKET NOT OPEN_BRACKET predicate CLOSE_BRACKET CLOSE_BRACKET OR some_predicates','some_predicates',8,'p_some_predicates','semantic.py',461),
  ('some_predicates -> OPEN_BRACKET NOT OPEN_BRACKET predicate CLOSE_BRACKET CLOSE_BRACKET','some_predicates',6,'p_some_predicates','semantic.py',462),
  ('while -> WHILE OPEN_BRACKET predicate CLOSE_BRACKET DO block','while',6,'p_while','semantic.py',476),
  ('while -> WHILE some_predicates DO block','while',4,'p_while','semantic.py',477),
  ('for -> FOR assignment TO arithmetic_expression DO block','for',6,'p_for','semantic.py',487),
  ('for -> FOR assignment DOWNTO arithmetic_expression DO block','for',6,'p_for','semantic.py',488),
  ('if -> IF OPEN_BRACKET predicate CLOSE_BRACKET THEN block','if',6,'p_if','semantic.py',495),
  ('if -> IF OPEN_BRACKET predicate CLOSE_BRACKET THEN block else','if',7,'p_if','semantic.py',496),
  ('else -> ELSE block','else',2,'p_else','semantic.py',506),
]