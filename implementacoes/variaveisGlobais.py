tabelaSimbolos = [
    # [tipoToken, lexema, valor, tipoDado] -> 2 ultimos serao preenchidos somente quando necessario
    ['relOp', '<', 'LT', ''],
    ['relOp', '>', 'GT', ''],
    ['relOp', '<=', 'LE', ''],
    ['relOp', '>=', 'GE', ''],
    ['relOp', '=', 'E', ''],
    ['relOp', '!=', 'DIFF', ''],
    ['int', 'int', '', ''],
    ['char', 'char', '', ''],
    ['float', 'float', '', ''],
    ['if', 'if', '', ''],
    ['then', 'then', '', ''],
    ['else', 'else', '', ''],
    ['while', 'while', '', ''],
    ['until', 'until', '', ''],
    ['repeat', 'repeat', '', ''],
    ['(', '(', '', ''],
    [')', ')', '', ''],
    ['{', '{', '', ''],
    ['}', '}', '', ''],
]

def varreTabela(lexema):
    pos = -1
    for i in tabelaSimbolos:
        if i[1] == lexema:
            pos = i.index
            break
    
    print(pos)

varreTabela('=')
