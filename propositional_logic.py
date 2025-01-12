"""
Propositional logic parser using [Parglare](https://github.com/igordejanovic/parglare).
Done this as an exercise while reading the book "Introduction to Logic" by Peter Smith (page 73)
"""
from parglare import Grammar, Parser

grammar = r"""
atom: LETTER | '!' atom | '(' atom BRELATION atom ')';

LETTER: P | Q | R | S;
BRELATION: AND | OR;

terminals
P: 'P';
Q: 'Q';
R: 'R';
S: 'S';
AND: '&';
OR: '|';
"""

actions = {
    'atom': [lambda _, nodes: f'{nodes[0]}',
             lambda _, nodes: f'¬{nodes[1]}',
             lambda _, nodes: f'({nodes[1]} {'∧' if nodes[2] == '&' else '∨'} {nodes[3]})'
             ],
}
parser = Parser(Grammar.from_string(grammar), build_tree=False, actions=actions)

def parse_forumla(formula):
    return parser.parse(formula)

print(parse_forumla('!((S & !P) | !(P & Q))'))
print(parse_forumla('Q'))

# Output:
# ¬((S ∧ ¬P) ∨ ¬(P ∧ Q))
# Q