from sly import Lexer, Parser

""""
Gramática:

PROGRAM −→ DEVICES CMDS
DEVICES −→ DEVICE DEVICES | DEVICE
DEVICE −→ dispositivo : {namedevice}
DEVICE −→ dispositivo : {namedevice, observation}
CMDS −→ CMD. CMDS | CMD.
CMD −→ ATTRIB | OBSACT | ACT
ATTRIB −→ set observation= VAR
OBSACT −→ se OBS entao ACT
OBSACT −→ se OBS entao ACT senao ACT
OBS −→ observation oplogic VAR
OBS −→ observation oplogic VAR && OBS
VAR −→ num bool
ACT −→ ACTION namedevice
ACT −→ enviar alerta (msg) namedevice
ACT −→ enviar alerta (msg, observation) namedevice
ACTION −→ ligar desligar

"""

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
        with open('saida.c', 'w') as fw:
            fw.write('#include <stdio.h>\n\n')

            fw.write('void ligar(char* namedevice) {\n\tprintf("%s ligado!\\n", namedevice);\n}\n\n')
            fw.write('void desligar(char* namedevice) {\n\tprintf("%s desligado!\\n", namedevice);\n}\n\n')
            fw.write('void alerta(char* namedevice, char* msg) {\n\tprintf("%s recebeu o alerta:\\n", namedevice);\n\tprintf("%s\\n", msg);\n}\n\n')
            fw.write('void alertaVariavel(char* namedevice, char* msg, int var) {\n\tprintf("%s recebeu o alerta:\\n", namedevice);\n\tprintf("%s %d\\n", msg, var);\n}\n\n') # Não sei se definir essa função com nome diferente vai impactar negativamente no desenvolvimento do trabalho

            fw.write('int main() {\n')

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
