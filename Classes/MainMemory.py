#CLASSE QUE REPRESENTA A MEMÓRIA PRINCIPAL (RANDOM ACCESS MEMORY) DO IAS#


class MainMemory:

    def __init__(self):
        # DEFINE 1000 POSIÇÕES NA MEMÓRIA PRINCIPAL (VETOR DE ÍNDICES 0 A 999)
        self.quantidadeEnderecosMemoria = 1000
        # DEFINE 40 POSIÇÕES EM CADA PALAVRA (VETOR DE ÍNDICES 0 A 39)
        self.quantidadeBitsPalavra = 40

        print('Memória Principal incializada...')

 # NOTA!! CRIAR UM VETOR (memoriaPrincial) QUE TERÁ 1000 POSICOES E EM CADA POSIÇÃO GUARDARÁ UM VETOR DE 40 POSIÇÕES, A IDEIA É SIMULAR A MEMORIA DO IAS (AS SUBCARACTERISTICAS DA PALAVRA IREI ESTUDAR DEPOIS A FUNDO)!