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
    tokens = {
        SET, OBSERVATION, NAMEDEVICE, IGUAL, NUM, PONTO,
        DISPOSITIVO, ABRECHAVES, FECHACHAVES, DOISPONTOS,
        VIRGULA, LIGAR, DESLIGAR, ENVIAR, ALERTA, ABREPARENTESES,
        FECHAPARENTESES, MENSAGEM, MAIOR, MENOR, MAIORIGUAL, MENORIGUAL,
        IGUALIGUAL, DIFERENTE, SE, ENTAO
    }
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
    ENVIAR = r'enviar'
    ALERTA = r'alerta'
    ABREPARENTESES = r'\('
    FECHAPARENTESES = r'\)'

    SE = r'se'
    ENTAO = r'entao'

    MAIORIGUAL = r'>='
    MENORIGUAL = r'<='
    IGUALIGUAL = r'=='
    DIFERENTE = r'!='
    MAIOR = r'>'
    MENOR = r'<'

    @_(r'[a-zA-Z_][a-zA-Z0-9_]*')
    def ID(self, t):
        if t.value[0].isupper():
            t.type = 'NAMEDEVICE'
        else:
            t.type = 'OBSERVATION'
        return t

    @_(r'"[^"]*"')
    def MENSAGEM(self, t):
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
        return f'// dispositivo declarado: {p.NAMEDEVICE}\n'
    
    @_('DISPOSITIVO DOISPONTOS ABRECHAVES NAMEDEVICE VIRGULA OBSERVATION FECHACHAVES')
    def comando(self, p):
        self.dispositivos.add(p.NAMEDEVICE)
        self.variaveis.add(p.OBSERVATION)
        return f'// dispositivo {p.NAMEDEVICE} com observação {p.OBSERVATION}\n'
    
    @_('LIGAR NAMEDEVICE PONTO')
    def comando(self, p):
        return f'ligar({p.NAMEDEVICE});'
    
    @_('DESLIGAR NAMEDEVICE PONTO')
    def comando(self, p):
        return f'desligar({p.NAMEDEVICE});'
    
    @_('ENVIAR ALERTA ABREPARENTESES MENSAGEM FECHAPARENTESES NAMEDEVICE')
    def comando(self, p):
        return f'alerta({p.NAMEDEVICE}, {p.MENSAGEM});'
    
    @_('ENVIAR ALERTA ABREPARENTESES MENSAGEM VIRGULA OBSERVATION FECHAPARENTESES NAMEDEVICE')
    def comando(self, p):
        return f'alertaVariavel({p.NAMEDEVICE}, {p.MENSAGEM}, {p.OBSERVATION});'
    
    @_('SE OBSERVATION MAIOR NUM ENTAO comando')
    def comando(self, p):
        return f'if ({p.OBSERVATION} > {p.NUM}) {{\n\t{p.comando}\n}}'
    
    @_('SE OBSERVATION MENOR NUM ENTAO comando')
    def comando(self, p):
        return f'if ({p.OBSERVATION} < {p.NUM}) {{\n\t{p.comando}\n}}'
    
    @_('SE OBSERVATION MAIORIGUAL NUM ENTAO comando')
    def comando(self, p):
        return f'if ({p.OBSERVATION} >= {p.NUM}) {{\n\t{p.comando}\n}}'
    
    @_('SE OBSERVATION MENORIGUAL NUM ENTAO comando')
    def comando(self, p):
        return f'if ({p.OBSERVATION} <= {p.NUM}) {{\n\t{p.comando}\n}}'


if __name__ == '__main__':
    lexer = ObsActLexer()
    parser = ObsActParser()

    erro = False
    #MUDANDO AQUI PARA TESTES!!!
    with open('Casos de Teste/teste10.obs') as f:
        entrada = f.read()

    try:
        tokens = list(lexer.tokenize(entrada))
        # print([t.type for t in tokens])  # debug
        saida = parser.parse(iter(tokens))
    except Exception as e:
        print(f'\n[ERRO] ao compilar: {e}')
        erro = True

    if not erro:
        with open('Casos de Teste/Saidas/outputTeste10.c', 'w') as fw:
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
                    fw.write(f'\t{linha}\n')
            elif saida is None:
                print("[ERRO] O parser não conseguiu entender a entrada.")
                exit(1)

            fw.write('\treturn 0;\n}\n')

        print("\n==============================")
        print("ObsAct compilado com sucesso!\n")
        print("Código gerado em outputTeste0X.c (X é o numero do teste)\n")
        print("==============================\n")

