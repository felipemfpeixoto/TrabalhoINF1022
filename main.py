from sly import Lexer, Parser

class ObsActLexer(Lexer):
    tokens = { SET, OBSERVATION, IGUAL, NUM, PONTO }
    ignore = ' \t'

    # Tokens literais
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
        print(f"Caractere ilegal '{t.value[0]}'")
        self.index += 1

class ObsActParser(Parser):
    tokens = ObsActLexer.tokens

    @_('SET OBSERVATION IGUAL NUM PONTO')
    def comando(self, p):
        return f'{p.OBSERVATION} = {p.NUM};'

if __name__ == '__main__':
    lexer = ObsActLexer()
    parser = ObsActParser()

    entrada = "set temperatura = 40 ."

    tokens = lexer.tokenize(entrada)
    codigo_c = parser.parse(tokens)

    with open('saida.c', 'w') as f:
        f.write('#include <stdio.h>\n\nint main() {\n')
        f.write(f'    int temperatura;\n')
        f.write(f'    {codigo_c}\n')
        f.write('    return 0;\n}')
    
    print("Código gerado com sucesso em 'saida.c'")
