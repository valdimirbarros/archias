#CLASSE QUE REPRESENTA O COMPUTADOR IAS#

from Classes.UnidadeCentralProcessamento import UnidadeCentralProcessamento
from Classes.MemoriaPrincipal import MemoriaPrincipal
from Classes.EntradaSaida import EntradaSaida

class Computador:

    def ligar(self):
        self.unidadeCentralProcessamento = UnidadeCentralProcessamento()
        self.unidadeCentralProcessamento.inicializar()
        self.memoria = MemoriaPrincipal()
        self.memoria.inicializar()
        self.entradaSaida = EntradaSaida()
        self.entradaSaida.inicializar()      
        print('Computador Ligado!')
    def desligar(self):
        #MATAR AS CLASSES UCP, MEMORIA PRINCIPAL E ENTRADASAIDA...
        print('Computador Desligado!')    
    def carregarPrograma(self):
        print('Carregando Programa...')
    def exibirResultado(self):
        self.entradaSaida.exibirResultado()
    def exibirCaracteristicas(self):
        self.entradaSaida.exibirCaracteristicasComputador(self.memoria.quantidadeEnderecosMemoria, self.memoria.quantidadeBitsPalavra)


#NOTA!! CONTINUA COM AS OUTRAS PARTES DO CODIGO E CHAMANDO O MODULO COMPUTADOR QUANDO NECESSARIO        

 

        

