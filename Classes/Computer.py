#CLASSE QUE REPRESENTA O COMPUTADOR IAS#

from Classes.ControlUnity import ControlUnity
from Classes.ArithmeticLogicUnit import ArithmeticLogicUnit

from Classes.MainMemory import MainMemory
from Classes.InputOutput import InputOutput

class Computer:

    def __init__(self):
        print('Computador Ligado! Carregando componentes...')
        self.controlUnity = ControlUnity() #INSTANCIA A UC
        self.arithmeticLogicUnit = ArithmeticLogicUnit() #INSTANCIA A ULA
        self.mainMemory = MainMemory() #INSTANCIA A MEMORIA PRINCIPAL
        self.inputOutput = InputOutput() #INSTANCIA ENTRADA E SAIDA
        print('Bem vindo ao Archias!')

    # -- MÉTODOS DO COMPUTADOR -- #
    
    def loadProgram(self,programName):
        program = open(programName,'r')
        for row in program:
            word = row.rstrip()
            opcode = word[0:8]
            address = word[8:20]
            if opcode == '11111111':
                print(address)
        program.close()

        print('Carregando Programa...')      

    def turnOff(self):
        #MATAR AS CLASSES UCP, MEMORIA PRINCIPAL E InputOutput...
        print('Computador Desligado! Até breve ...')      
    


    # -- MÉTODOS DOS MODULOS DO COMPUTADOR -- #

    #UNIDADE DE CONTROLE 
    def controlUnityWriteInMemory(self):
        self.controlUnity.writeInMemory(self.mainMemory,2, [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
    def controlUnityReadInMemory(self):
        self.controlUnity.readInMemory(self.mainMemory,2)  
    
    #UNIDADE LOGICA E ARITMETICA

    #MEMORIA PRINCIPAL
    def goThroughMainMemory(self):
        self.mainMemory.goThroughMainMemory()

    #ENTRADA E SAIDA
    def showResult(self):
        self.inputOutput.showResult()
    def showSpecifications(self):
        self.inputOutput.showSpecifications(self.mainMemory.amountMemoryAddresses, self.mainMemory.amountBitsWord)
    
            





 
'''
O PROGRAMA.TXT VAI ENVIAR INSTRUCOES QUE VAO SE COMUNICAR COM A CLASSE DE COMPUTADOR.PY 
E ESTA VAI ACESSAR OS DEMAIS COMPONENTES DO COMPUTADOR COMO UC ULA MAINMEMORY E IO 

#NOTA!! AGORA JA LEIO ARQUIVO E TRABALHO COM SUAS STRINGS FALTA VER O FUNCIONAMENTO DESSAS STRINGS PRA MANIPULAR O PROGRAMA      
'''        

