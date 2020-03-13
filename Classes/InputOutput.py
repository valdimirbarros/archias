#CLASSE QUE REPRESENTA OS DISPOSITIVOS DE ENTRADA E SAÍDA DE DADOS (INPUT OUTPUT SYSTEM) DO IAS#
import webbrowser
import json


class InputOutput:
    def __init__(self):
        print('Dispositivos de Entrada e Saída incializados...')
        #webbrowser.open("C:/wamp64/www/UFMA/archias/View/archias.html", new=1)

    #def findTbody(self):
          

    #def changeLine(self, indexLinha, novaLinha):
         

    def showResult(self):
        print('Exibindo resultado do programa no navegador padrão instalado...')

        with open('./Archias/View/result.html','r') as f:
            texto=f.readlines()
        for i in texto:
            if '<tbody>' in i:
                print(texto.index(i))
                return
        print('String não encontrada') 
        arquivo = open('./Archias/View/result.html','w')
        arquivo.seek(0)
        arquivo.write('aASDASDSA')       
        arquivo.close()


        #webbrowser.open("C:/wamp64/www/UFMA/archias/View/result.html", new=1)

    def showSpecifications(self, quantidadeEnderecosMemoria, quantidadeBitsPalavra):
        print('Este Computador Possui ' +
              str(quantidadeEnderecosMemoria) + ' posições de memória')
        print('Este Computador Possui palavras de ' +
              str(quantidadeBitsPalavra) + ' bits')


# NOTA!!1 REFLETIR SE VALE A PENA OU NAO PASSAR A ABERTURA DO BROWSER NO METODO INICILIZAR PARA UMA FUNÇÃO MAIS ATRAENTE...
# NOTA!!2 BUSCAR UMA FORMA PARA GRAVAR UM ARQUIVO JSON NO DIRETÓRIO (SAIDA DE RESULTADOS )PARA SER LIDO PELO NAVEGADOR TALVEZ UMA RESPOSTA AO CLIENTE VOU VER AINDA COMO FACO NAO QQUERO USAR NADA DE HTTP MAS FAZER OQUE NÉ MANO
