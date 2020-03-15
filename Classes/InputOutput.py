#CLASSE QUE REPRESENTA OS DISPOSITIVOS DE ENTRADA E SAÍDA DE DADOS (INPUT OUTPUT SYSTEM) DO IAS#
import webbrowser
import json


class InputOutput:
    def __init__(self):
        print('Dispositivos de Entrada e Saída incializados...')
        #webbrowser.open("C:/wamp64/www/UFMA/archias/View/archias.html", new=1)

 
    def showResult(self):
        print('Exibindo resultado do programa...')
        #webbrowser.open("C:/wamp64/www/UFMA/archias/View/result.html", new=1)

    def showSpecifications(self, amountMemoryAddresses, amountBitsWord):
        print('Este Computador Possui {} posições de memória'.format(amountMemoryAddresses))
        print('Este Computador Possui palavras de {} bits'.format(amountBitsWord))

    




# NOTA!!1 REFLETIR SE VALE A PENA OU NAO PASSAR A ABERTURA DO BROWSER NO METODO INICILIZAR PARA UMA FUNÇÃO MAIS ATRAENTE...
# NOTA!!2 BUSCAR UMA FORMA PARA GRAVAR UM ARQUIVO JSON NO DIRETÓRIO (SAIDA DE RESULTADOS )PARA SER LIDO PELO NAVEGADOR TALVEZ UMA RESPOSTA AO CLIENTE VOU VER AINDA COMO FACO NAO QQUERO USAR NADA DE HTTP MAS FAZER OQUE NÉ MANO
