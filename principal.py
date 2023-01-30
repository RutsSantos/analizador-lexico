from buffer import Buffer
from analizador import AnalizadorLexico

if __name__ == '__main__':
    Buffer = Buffer()
    Analizador = AnalizadorLexico()

    token = []
    lexeme = []
    row = []
    column = []

    for i in Buffer.load_buffer():
        t, lex, lin, col = Analizador.tokenize(i)
        token += t
        lexeme += lex
        row += lin
        column += col

    print('\nTokens reconocidos: ', token)
