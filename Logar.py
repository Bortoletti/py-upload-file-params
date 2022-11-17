# Logar.py
# Bortoletti, Luis Alexandre
#
# Classe para gerar logs
#
#    Ao instanciar a classe Logar é definido o timestamp e sequencia do aqrquivo que controla
# as mensagens desse log, onde a sequencia é um numero randmomico para
# diferenciar aquivos que sejam gerados pela mesma rotina no mesmo momento.
#    Todas as mensagens tem seu timestamp no inicio da linha.
#
# Requisitos:
# - pasta logs
#
#
# exemplo:
# logar = Logar("nomeArquivo")
# logar.escrever("mensagem")
#
#================================================
#import os
from datetime import datetime
import random

class Logar:
    arquivo = ""
    tsarquivo = ""
    sequencia = 0 
    linhas = 0
    def __init__( self, arquivoP ):
        # print("inicio")
        self.arquivo = arquivoP
        self.tsarquivo = datetime.now().strftime("%Y%m%d-%H%M%S")
        self.sequencia =   random.randrange( 2345,899976)

    def escrever( self, mensagemP ):
        # print("escrever") 
        horario = datetime.now().strftime("%Y%m%d-%H%M%S")    
        f = open( f"logs/{self.arquivo}-{self.tsarquivo}-{self.sequencia}.txt", "a")
        if( self.linhas > 0 ):
          f.write( f"\n")
        f.write( f"#{horario}:{mensagemP}")
        f.close()
        self.linhas += 1

