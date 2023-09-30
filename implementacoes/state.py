import string

numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alfabeto = list(string.ascii_letters)
letras = [alfabeto]


class Estado:
    # estado0 = (0, False, [1, 3], False, None)
    def __init__(self, nome: int, final: bool, transicoes, lookahead: bool, retornoToken):
        self.nome = nome
        self.final = final
        self.transicoes = transicoes
        self.lookahead = lookahead
        self.retornoToken = retornoToken


def defineTabelaTransicao():
    tabelaTransicao = [
        Estado(
            nome=-1,
            final=True,
            transicoes=[],
            lookahead=False,
            retornoToken='_'
        ),

        Estado(
            nome=0,
            final=False,
            transicoes=[
                (numeros, 3),
                (letras, 1),
                (' ' or '\n' or '\t', 21),
                ('<', 12),
                ('>', 15),
                ('!', 18),
                ('=', 20),
                ('{', 23)
            ],
            lookeahead=False,
            retornoToken=None
        ),

        Estado(
            nome=1,
            final=False,
            transicoes=[
                (letras, 1),
                (numeros, 2)
            ],
            lookahead=False,
            retornoToken=None
        ),

        Estado(
            nome=2,
            final=True,
            transicoes=[],
            lookahead=True,
            retornoToken='_'
        ),

        Estado(
            nome=3,
            final=False,
            transicoes=[
                (numeros, 3),
                ('.', 5),
                ('E', 8),
                (not numeros and not '.' and not 'E', 4)
            ],
            lookahead=False,
            retornoToken=None
        ),
        
        Estado(
            nome=4,
            final=True,
            transicoes=[],
            lookahead=True,
            retornoToken='_'
        ),

        Estado(
            nome=5,
            final=True,
            transicoes=[
                (numeros, 6),
                (not numeros, -1)
            ],
            lookahead=False,
            retornoToken=None
        ),

        Estado(
            nome=6,
            final=False,
            transicoes=[
                (numeros, 6),
                ('E', 8),
                (not numeros and not 'E', 7)
            ],
            lookahead=False,
            retornoToken=None
        ),

        Estado(
            nome=7,
            final=True,
            transicoes=[],
            lookahead=True,
            retornoToken='_'
        ),

        Estado(
            nome=8,
            final=False,
            transicoes=[
                ('+', 9),
                ('-', 9),
                (numeros, 10),
                (not '+' and not '-' and not numeros, -1)
            ],
            lookahead=False,
            retornoToken=None
        ),

        Estado(
            nome=9,
            final=False,
            transicoes=[
                (numeros, 10),
                (not numeros, -1)
            ],
            lookahead=False,
            retornoToken=None
        ),

        Estado(
            nome=10,
            final=False,
            transicoes=[
                (numeros, 10),
                (not numeros, 11)
            ],
            lookahead=False,
            retornoToken=None
        ),

        Estado(
            nome=11,
            final=True,
            transicoes=[],
            lookahead=True,
            retornoToken='_'
        ),
        
        Estado(
            nome=12,
            final=False,
            transicoes=[
                ('=', 13),
                (not '=', 14)
            ],
            lookahead=False,
            retornoToken=None
        ),

        Estado(
            nome=13,
            final=True,
            transicoes=[],
            lookahead=False,
            retornoToken='LE'
        ),

        Estado(
            nome=14,
            final=True,
            transicoes=[],
            lookahead=True,
            retornoToken='LT'
        ),

        Estado(
            nome=15,
            final=False,
            transicoes=[
                ('=', 16),
                (not '=', 17)
            ],
            lookahead=False,
            retornoToken=None
        ),

        Estado(
            nome=16,
            final=True,
            transicoes=[],
            lookahead=False,
            retornoToken='GE'
        ),

        Estado(
            nome=17,
            final=True,
            transicoes=[],
            lookahead=True,
            retornoToken='GT'
        ),

        Estado(
            nome=18,
            final=False,
            transicoes=[
                ('=', 19),
                (not '=', -1)
            ],
            lookahead=False,
            retornoToken=None
        ),

        Estado(
            nome=19,
            final=True,
            transicoes=[],
            lookahead=False,
            retornoToken='DIFF'
        ),

        Estado(
            nome=20,
            final=True,
            transicoes=[],
            lookahead=False,
            retornoToken='EQ'
        ),

        Estado(
            nome=21,
            final=False,
            transicoes=[
                (' ' or '\n' or '\t', 21),
                (not ' ' and not '\n' and not '\t', -1)
            ],
            lookahead=False,
            retornoToken=None
        ),
        
        Estado(
            nome=22,
            final=True,
            transicoes=[],
            lookahead=True,
            retornoToken='_'
        ),

        Estado(
            nome=23,
            final=False,
            transicoes=[
                ('}', 24),
                (not '}' and not '{', 23)
            ],
            lookahead=False,
            retornoToken=None
        ),

        Estado(
            nome=24,
            final=True,
            transicoes=[],
            lookahead=False,
            retornoToken='_'
        ),

        Estado(
            nome=25,
            final=True,
            transicoes=[],
            lookahead=False,
            retornoToken='_'
        ),

        Estado(
            nome=26,
            final=True,
            transicoes=[],
            lookahead=False,
            retornoToken='_'
        ),

        Estado(
            nome=27,
            final=True,
            transicoes=[],
            lookahead=False,
            retornoToken='_'
        ),

        Estado(
            nome=28,
            final=True,
            transicoes=[],
            lookahead=False,
            retornoToken='_'
        ),

        Estado(
            nome=29,
            final=True,
            transicoes=[],
            lookahead=False,
            retornoToken='_'
        ),

        Estado(
            nome=30,
            final=True,
            transicoes=[],
            lookahead=False,
            retornoToken='_'
        ),

        Estado(
            nome=31,
            final=True,
            transicoes=[],
            lookahead=False,
            retornoToken='_'
        ),

        Estado(
            nome=32,
            final=True,
            transicoes=[],
            lookahead=False,
            retornoToken='_'
        ),

        Estado(
            nome=33,
            final=True,
            transicoes=[],
            lookahead=False,
            retornoToken='_'
        ),

    ]
