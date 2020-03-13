#CLASSE QUE REPRESENTA O COMPUTADOR IAS#

from Classes.ControlProcessUnity import ControlProcessUnity
from Classes.MainMemory import MainMemory
from Classes.InputOutput import InputOutput

class Computer:

    def turnOn(self):
        self.controlProcessUnity = ControlProcessUnity() #INSTANCIA A UCP
        self.memory = MainMemory() #INSTANCIA A MEMORIA PRINCIPAL
        self.inputOutput = InputOutput() #INSTANCIA ENTRADA E SAIDA
        print('Computador Ligado!')
    def turnOff(self):
        #MATAR AS CLASSES UCP, MEMORIA PRINCIPAL E InputOutput...
        print('Computador Desligado!')    
    def loadProgram(self):
        print('Carregando Programa...')
    def showResult(self):
        self.inputOutput.showResult()
    def showSpecifications(self):
        self.inputOutput.showSpecifications(self.memory.quantidadeEnderecosMemoria, self.memory.quantidadeBitsPalavra)


#NOTA!! CONTINUA COM AS OUTRAS PARTES DO CODIGO E CHAMANDO O MODULO Computer QUANDO NECESSARIO        

 

        

