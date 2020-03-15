#CLASSE QUE REPRESENTA A UNIDADE DE CONTROLE  (UC) DO IAS#


class ControlUnity:

    def __init__(self):
        # -- CARACTERISTICAS DA UNIDADE DE CONTROLE  -- #
        #REGISTRADORES
        self.PC = ''  # Program Counter
        self.MAR = ''  # Memory Address Register
        self.IR = ''  # Instruction Register
        self.IBR = ''  # o Instruction Buffer Register
        print('Unidade de Controle inicializada...')

    # -- MÉTODOS DA UNIDADE DE CONTROLE  -- #

    def writeInMemory(self, mainMemory, address, data):
        print('Unidade de Controle ESCREVENDO dados na memória na posição: ', address)
        mainMemory.mainMemory[address] = data

    def readInMemory(self, mainMemory, address):
        print('Unidade de Controle LENDO dados na memória  na posição: ', address)
        print(address, mainMemory.mainMemory[address])

        
