tabelaSimbolos = [
    # [tipoToken, lexema, valor, tipoDado] -> 2 ultimos serao preenchidos somente quando necessario
    ['relOp', '<', 'LT', None],
    ['relOp', '>', 'GT', None],
    ['relOp', '<=', 'LE', None],
    ['relOp', '>=', 'GE', None],
    ['relOp', '=', 'E', None],
    ['relOp', '!=', 'DIFF', None],
    ['+', '+', None, None],
    ['-', '-', None, None],
    ['*', '*', None, None],
    ['/', '/', None, None],
    [':=', ':=', None, None],
    [';', ';', None, None],
    ['.', '.', None, None],
    ['(', '(', None, None],
    [')', ')', None, None],
    ['{', '{', None, None],
    ['}', '}', None, None],
]


# keywords
keywords = ['int', 'char', 'float', 'if', 'then', 'else', 'while', 'until', 'repeat', 'program', 'begin', 'end']
listaTokens = []
digitos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letras = ['a']

def isKeyword(lexema):
    return lexema in keywords



def estadoInicial():
    return 0

def estadoFinal(estado):
    if estado != 2:
        return False
    else:
        return True

# Verifica se eh uma letra do alfabeto
def ehAZ(caractere):
    if (ord('a') <= ord(caractere) <= ord('z')) or (ord('A') <= ord(caractere) <= ord('Z')):
        return True
    else:
        return False


# Verifica se eh um digito de 0 a 9
def ehNumero(caractere):
    if ord('0') <= ord(caractere) <= ord('9'):
        return True
    else:
        return False


# Verifica se eh um separador
def ehSeparador(caractere):
    if caractere == '\n' or caractere == ' ':
        return True
    else:
        return False


def move(estado, caractere):
    # Para ID's
    if estado == 0 and ehAZ(caractere):
        return 1
    elif estado > 0 and (ehAZ(caractere) or ehNumero(caractere)):
        if estado == 1:
            return 1
    elif estado > 0 and ehSeparador(caractere):
        return 2 # Estado final
    else:
        return -1

    # if ehAZ(caractere) or ehNumero(caractere) and estado >= 0:
    #     if estado == 0 and ehAZ(caractere) == False:
    #         return -1
    #     elif estado == 0:
    #         return 1
    #     elif estado == 1 or estado == 2:
    #         return 2
    # elif caractere != '\n' and caractere != ' ' and caractere != '_':
    #     return -1
    # else:
    #     return 3
    