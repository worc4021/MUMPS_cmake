grammar make;

file: content* EOF;

content
    : assignment NEWLINE
    | recipe
    | NEWLINE
    | WORD filename NEWLINE
    ;

recipe
    : '.' WORD '.' WORD  ':' NEWLINE (commands NEWLINE)* #specialRecipe
    | target ':' dependents NEWLINE (commands NEWLINE)* #regularRecipe
    ;

target: filename;

dependents: dependent*
        ;

dependent: filename #usefulDependent
    | continued #uselessDependent
    ;

assignment: varname '=' assignee+;

varname: WORD;

assignee: continued #uselessAssignee
        | filename  #usefulAssignee
        ;

continued: BACKSLASH NEWLINE;

commands: command+;

command: WORD 
    | filename  
    | FLAG 
    | STRING
    | BASHOP
    | assignment
    | continued
    ;


filename: WORD ('.' WORD)*
        | '..'
        | '.' WORD
    ;
    
WORD: ('$' |'(' | ')' | '@' | '?' | '<' | '^' | '%' | '*' | '/' | [a-zA-Z0-9_]+)+;

BACKSLASH: '\\';

STRING: '"' (~[\r\n"] | '\\' .)* '"';

BASHOP: '|' | ';' | '>' | '*';

FLAG: '-' (~[ ])+;

COMMENT: '#' (~[\r\n])* NEWLINE -> skip;

NEWLINE: '\r'? '\n';

WS: [ \t]+ -> skip;