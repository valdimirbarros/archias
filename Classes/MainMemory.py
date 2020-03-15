#CLASSE QUE REPRESENTA A MEMÓRIA PRINCIPAL (RANDOM ACCESS MEMORY) DO IAS#

class MainMemory:

    def __init__(self):
        # -- CARACTERISTICAS DA MEMÓRIA PRINCIPAL -- #
        self.amountBitsWord = 40 #QUANTIDADE DE BITS POR PALAVRA
        self.amountMemoryAddresses = 1000 #QUANTIDADE DE DE ENDEREÇOS DA MEMÓRIA
        self.bitsWord = [0 for x in range(0,self.amountBitsWord)] # DEFINE 40 POSIÇÕES EM CADA PALAVRA (VETOR DE ÍNDICES 0 A 39)
        self.mainMemory = [self.bitsWord for x in range(0,self.amountMemoryAddresses)] # DEFINE 1000 POSIÇÕES NA MEMÓRIA PRINCIPAL (VETOR DE ÍNDICES 0 A 999 QUE GUARDA O VETOR DE PALAVRAS)
        print('Memória Principal incializada...')

    # -- MÉTODOS DA MEMÓRIA PRINCIPAL -- #
    def goThroughMainMemory(self):
        print('######---------------------------MEMÓRIA PRINCIPAL-------------------------#########')
        for address, cell in enumerate(self.mainMemory):
            print(address , cell)
