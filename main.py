from sly import Lexer, Parser

class ObsActLexer(Lexer):
    tokens = { SET, OBSERVATION, IGUAL, NUM, PONTO }
    ignore = ' \t'

    SET = r'set'
    IGUAL = r'='
    PONTO = r'\.'
    NUM = r'[0-9]+'

    @_(r'[a-zA-Z][a-zA-Z0-9]*')
    def OBSERVATION(self, t):
        return t

    ignore_newline = r'\n+'
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print(f"[LEXER] Caractere ilegal: '{t.value[0]}'")
        self.index += 1

class ObsActParser(Parser):
    tokens = ObsActLexer.tokens

    def __init__(self):
        self.variaveis = set()  # Armazena os nomes de variáveis usados

    @_('SET OBSERVATION IGUAL NUM PONTO')
    def comando(self, p):
        self.variaveis.add(p.OBSERVATION)
        return f'{p.OBSERVATION} = {p.NUM};'

if __name__ == '__main__':
    lexer = ObsActLexer()
    parser = ObsActParser()

    linhas_convertidas = []
    erro = False

    with open('programa.obs') as f:
        linhas = f.readlines()

    for idx, linha in enumerate(linhas):
        if linha.strip() == "":
            continue
        try:
            tokens = lexer.tokenize(linha)
            saida = parser.parse(tokens)
            if saida:
                linhas_convertidas.append(saida)
        except Exception as e:
            print(f'\n[ERRO] na linha {idx+1} ::: {linha.strip()!r}')
            erro = True
            break

    if not erro:
        with open('programa.c', 'w') as fw:
            fw.write('#include <stdio.h>\n\nint main() {\n')

            # Declara as variáveis identificadas
            for var in sorted(parser.variaveis):
                fw.write(f'    int {var} = 0;\n')

            fw.write('\n')
            for linha in linhas_convertidas:
                fw.write(f'    {linha}\n')

            fw.write('    return 0;\n}\n')

        print("\n==============================")
        print("ObsAct compilado com sucesso!")
        print("Código gerado em programa.c")
        print("==============================\n")
