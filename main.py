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
from sly import Lexer, Parser

class ObsActLexer(Lexer):
    tokens = { SET, OBSERVATION, NAMEDEVICE, IGUAL, NUM, PONTO,
               DISPOSITIVO, ABRECHAVES, FECHACHAVES, DOISPONTOS, VIRGULA, LIGAR, DESLIGAR }
    ignore = ' \t'

    SET = r'set'
    IGUAL = r'='
    PONTO = r'\.'
    NUM = r'[0-9]+'
    DISPOSITIVO = r'dispositivo'
    ABRECHAVES = r'\{'
    FECHACHAVES = r'\}'
    DOISPONTOS = r':'
    VIRGULA = r','
    LIGAR = r'ligar'
    DESLIGAR = r'desligar'

    @_(r'[A-Z_][a-zA-Z0-9_]*')
    def NAMEDEVICE(self, t):
        return t

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
    start = 'programa'

    def __init__(self):
        self.variaveis = set()
        self.dispositivos = set()

    @_('linhas')
    def programa(self, p):
        return '\n'.join(p.linhas)

    @_('linhas comando')
    def linhas(self, p):
        return p.linhas + [p.comando]

    @_('comando')
    def linhas(self, p):
        return [p.comando]

    @_('SET OBSERVATION IGUAL NUM PONTO')
    def comando(self, p):
        self.variaveis.add(p.OBSERVATION)
        return f'{p.OBSERVATION} = {p.NUM};'

    @_('DISPOSITIVO DOISPONTOS ABRECHAVES NAMEDEVICE FECHACHAVES')
    def comando(self, p):
        self.dispositivos.add(p.NAMEDEVICE)
        return f'// dispositivo declarado: {p.NAMEDEVICE}'
    
    @_('DISPOSITIVO DOISPONTOS ABRECHAVES NAMEDEVICE VIRGULA OBSERVATION FECHACHAVES')
    def comando(self, p):
        self.dispositivos.add(p.NAMEDEVICE)
        self.variaveis.add(p.OBSERVATION)
        return f'// dispositivo {p.NAMEDEVICE} com observação {p.OBSERVATION}'
    
    @_('LIGAR NAMEDEVICE PONTO')
    def comando(self, p):
        return f'ligar({p.NAMEDEVICE});'
    
    @_('DESLIGAR NAMEDEVICE PONTO')
    def comando(self, p):
        return f'desligar({p.NAMEDEVICE});'


if __name__ == '__main__':
    lexer = ObsActLexer()
    parser = ObsActParser()

    erro = False
    with open('programa.obs') as f:
        entrada = f.read()

    try:
        tokens = list(lexer.tokenize(entrada))
        saida = parser.parse(iter(tokens))
    except Exception as e:
        print(f'\n[ERRO] ao compilar: {e}')
        erro = True

    if not erro:
        with open('saida.c', 'w') as fw:
            fw.write('#include <stdio.h>\n\n')

            # Funções auxiliares
            fw.write('void ligar(char* namedevice) {\n\tprintf("%s ligado!\\n", namedevice);\n}\n\n')
            fw.write('void desligar(char* namedevice) {\n\tprintf("%s desligado!\\n", namedevice);\n}\n\n')
            fw.write('void alerta(char* namedevice, char* msg) {\n\tprintf("%s recebeu o alerta:\\n", namedevice);\n\tprintf("%s\\n", msg);\n}\n\n')
            fw.write('void alertaVariavel(char* namedevice, char* msg, int var) {\n\tprintf("%s recebeu o alerta:\\n", namedevice);\n\tprintf("%s %d\\n", msg, var);\n}\n\n')

            # Dispositivos
            for dispositivo in sorted(parser.dispositivos):
                fw.write(f'char {dispositivo}[100] = "{dispositivo}";\n')

            fw.write('\nint main() {\n')

            for var in sorted(parser.variaveis):
                fw.write(f'    int {var} = 0;\n')

            fw.write('\n')
            if saida:
                for linha in saida.split('\n'):
                    fw.write(f'    {linha}\n')
            elif saida is None:
                print("[ERRO] O parser não conseguiu entender a entrada.")
                exit(1)

            fw.write('    return 0;\n}\n')

        print("\n==============================")
        print("ObsAct compilado com sucesso!")
        print("Código gerado em saida.c")
        print("==============================\n")

