#CLASSE QUE REPRESENTA OS DISPOSITIVOS DE ENTRADA E SAÍDA DE DADOS (INPUT OUTPUT SYSTEM) DO IAS#
import webbrowser
import json


class EntradaSaida:
    def inicializar(self):
        print('Dispositivos de Entrada e Saída incializados...')
        webbrowser.open("C:/wamp64/www/UFMA/archias/Exibicao/archias.html", new=1)

    def exibirResultado(self):
        print('Exibindo resultado do programa no navegador padrão instalado...')
        f = open('obj.json', 'w')
        f.write('This is a test\n')
        f.close()
        # objJson = json.dumps([1, 'simple', 'list'])
        # json.dump(json, arquivo)

        webbrowser.open(
            "C:/wamp64/www/UFMA/archias/Exibicao/resultado.html", new=1)

    def exibirCaracteristicasComputador(self, quantidadeEnderecosMemoria, quantidadeBitsPalavra):
        print('Este Computador Possui ' +
              str(quantidadeEnderecosMemoria) + ' posições de memória')
        print('Este Computador Possui palavras de ' +
              str(quantidadeBitsPalavra) + ' bits')


# NOTA!!1 REFLETIR SE VALE A PENA OU NAO PASSAR A ABERTURA DO BROWSER NO METODO INICILIZAR PARA UMA FUNÇÃO MAIS ATRAENTE...
# NOTA!!2 BUSCAR UMA FORMA PARA GRAVAR UM ARQUIVO JSON NO DIRETÓRIO (SAIDA DE RESULTADOS )PARA SER LIDO PELO NAVEGADOR TALVEZ UMA RESPOSTA AO CLIENTE VOU VER AINDA COMO FACO NAO QQUERO USAR NADA DE HTTP MAS FAZER OQUE NÉ MANO
