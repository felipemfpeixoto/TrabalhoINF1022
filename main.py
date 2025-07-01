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
        IGUALIGUAL, DIFERENTE, SE, ENTAO, BOOL, ECOMERCIAL, SENAO, PARA, TODOS
    }
    ignore = ' \t'

    SET = r'set'
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

    SENAO = r'senao'
    SE = r'se'
    ENTAO = r'entao'

    MAIORIGUAL = r'>='
    MENORIGUAL = r'<='
    IGUALIGUAL = r'=='
    IGUAL = r'='
    DIFERENTE = r'!='
    MAIOR = r'>'
    MENOR = r'<'

    BOOL = r'TRUE|FALSE'

    ECOMERCIAL = r'&&'

    PARA = r'para'
    TODOS = r'todos'

    @_(r'[a-zA-Z][a-zA-Z0-9]*')
    def ID(self, t):
        if t.value.isalpha() and t.value[0].isupper():
            t.type = 'NAMEDEVICE'
        else:
            t.type = 'OBSERVATION'
        return t

    @_(r'"[^"].*"')
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

    def zera_tudo(self):
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

    # MARK: Comandos

    @_('ENVIAR ALERTA ABREPARENTESES MENSAGEM FECHAPARENTESES PARA TODOS DOISPONTOS lista_dispositivos PONTO')
    def comando(self, p):
        for dev in p.lista_dispositivos:
            if dev not in self.dispositivos:
                print(f"[ERRO] Dispositivo '{dev}' nao declarado.")
        linhas = [f'alerta({dev}, {p.MENSAGEM});' for dev in p.lista_dispositivos]
        return '\n'.join(linhas)

    @_('NAMEDEVICE')
    def lista_dispositivos(self, p):
        return [p.NAMEDEVICE]

    @_('NAMEDEVICE VIRGULA lista_dispositivos')
    def lista_dispositivos(self, p):
        return [p.NAMEDEVICE] + p.lista_dispositivos


    # MARK: (Comandos) Sets

    @_('SET OBSERVATION IGUAL NUM PONTO')
    def comando(self, p):
        self.variaveis.add(p.OBSERVATION)
        return f'{p.OBSERVATION} = {p.NUM};'

    @_('SET OBSERVATION IGUAL BOOL PONTO')
    def comando(self, p):
        self.variaveis.add(p.OBSERVATION)
        valor = '1' if p.BOOL == 'TRUE' else '0'
        return f'{p.OBSERVATION} = {valor};'
    
    # MARK: (Comandos) Declaracao de dispositivos

    @_('DISPOSITIVO DOISPONTOS ABRECHAVES NAMEDEVICE FECHACHAVES')
    def comando(self, p):
        self.dispositivos.add(p.NAMEDEVICE)
        return f'// dispositivo declarado: {p.NAMEDEVICE}\n'

    @_('DISPOSITIVO DOISPONTOS ABRECHAVES NAMEDEVICE VIRGULA OBSERVATION FECHACHAVES')
    def comando(self, p):
        self.dispositivos.add(p.NAMEDEVICE)
        self.variaveis.add(p.OBSERVATION)
        return f'// dispositivo {p.NAMEDEVICE} com observação {p.OBSERVATION}\n'
    

    # MARK: (Comandos) Ligar/Desligar Dispositivos

    @_('LIGAR NAMEDEVICE PONTO')
    def comando(self, p):
        return f'ligar({p.NAMEDEVICE});'

    @_('DESLIGAR NAMEDEVICE PONTO')
    def comando(self, p):
        return f'desligar({p.NAMEDEVICE});'
    
    # MARK: (Comandos) Enviar Alertas

    @_('ENVIAR ALERTA ABREPARENTESES MENSAGEM FECHAPARENTESES NAMEDEVICE PONTO')
    def comando(self, p):
        return f'alerta({p.NAMEDEVICE}, {p.MENSAGEM});'

    @_('ENVIAR ALERTA ABREPARENTESES MENSAGEM VIRGULA OBSERVATION FECHAPARENTESES NAMEDEVICE PONTO')
    def comando(self, p):
        return f'alertaVariavel({p.NAMEDEVICE}, {p.MENSAGEM}, {p.OBSERVATION});'
    

    # MARK: (Comandos) Condicionais
    
    @_('SE observacao ENTAO comando SENAO comando') # Agora está funcionando, porém, precisamos por um ponto após cada comando, assim como ; em C
    def comando(self, p):
        return f'if ({p.observacao}) {{\n\t{p.comando0}\n}} else {{\n\t{p.comando1}\n}}'

    @_('SE observacao ENTAO comando')
    def comando(self, p):
        return f'if ({p.observacao}) {{\n\t{p.comando}\n}}'
    
    # MARK: Observacao

    @_('OBSERVATION operador_logico valor')
    def observacao(self, p):
        self.variaveis.add(p.OBSERVATION)
        return f'({p.OBSERVATION} {p.operador_logico} {p.valor})'

    @_('OBSERVATION operador_logico valor ECOMERCIAL observacao')
    def observacao(self, p):
        self.variaveis.add(p.OBSERVATION)
        return f'({p.OBSERVATION} {p.operador_logico} {p.valor}) && {p.observacao}'
    
    # MARK: Valores

    @_('NUM')
    def valor(self, p):
        return p.NUM

    @_('BOOL')
    def valor(self, p):
        return '1' if p.BOOL == 'TRUE' else '0'
    
    # MARK: Operadores Lógicos

    @_('MAIOR')
    def operador_logico(self, p):
        return '>'

    @_('MENOR')
    def operador_logico(self, p):
        return '<'

    @_('MAIORIGUAL')
    def operador_logico(self, p):
        return '>='

    @_('MENORIGUAL')
    def operador_logico(self, p):
        return '<='

    @_('IGUALIGUAL')
    def operador_logico(self, p):
        return '=='

    @_('DIFERENTE')
    def operador_logico(self, p):
        return '!='



if __name__ == '__main__':
    lexer = ObsActLexer()
    parser = ObsActParser()

    erro = False
    #MUDANDO AQUI PARA TESTES!!!

    for i in range(1, 16):
        parser.zera_tudo()

        testIndex = (i if i > 9 else f'0{i}')
        testeFilename = f'teste{testIndex}.obs'
        outputFilename = f'outputTeste{testIndex}.c'
        with open('Casos de Teste/' +testeFilename) as f:
            entrada = f.read()

        try:
            tokens = list(lexer.tokenize(entrada))
            # print([t.type for t in tokens])  # debug
            saida = parser.parse(iter(tokens))
        except Exception as e:
            print(f'\n[ERRO] ao compilar: {e}')
            erro = True

        if not erro:
            outputPath = f'Casos de Teste/Saidas/{outputFilename}'
            with open(outputPath, 'w') as fw:
                fw.write('#include <stdio.h>\n\n')

                # Funções auxiliares
                fw.write('void ligar(char* namedevice) {\n\tprintf("%s ligado!\\n", namedevice);\n}\n\n')
                fw.write('void desligar(char* namedevice) {\n\tprintf("%s desligado!\\n", namedevice);\n}\n\n')
                fw.write('void alerta(char* namedevice, char* msg) {\n\tprintf("%s recebeu o alerta:\\n", namedevice);\n\tprintf("%s\\n", msg);\n}\n\n')
                fw.write('void alertaVariavel(char* namedevice, char* msg, unsigned int var) {\n\tprintf("%s recebeu o alerta:\\n", namedevice);\n\tprintf("%s %d\\n", msg, var);\n}\n\n')

                # Dispositivos
                for dispositivo in sorted(parser.dispositivos):
                    fw.write(f'char {dispositivo}[100] = "{dispositivo}";\n')

                fw.write('\nint main() {\n')

                for var in sorted(parser.variaveis):
                    fw.write(f'    unsigned int {var} = 0;\n')

                fw.write('\n')
                if saida:
                    for linha in saida.split('\n'):
                        fw.write(f'\t{linha}\n')
                elif saida is None:
                    print("[ERRO] O parser não conseguiu entender a entrada.")
                    exit(1)

                fw.write('\treturn 0;\n}\n')

            print("\n==============================")
            print("ObsAct compilado com sucesso!")
            print("Código gerado em %s (X é o numero do teste)" % (outputFilename))
            print("==============================")

        # Compilando e executando arquivos compilados
        

