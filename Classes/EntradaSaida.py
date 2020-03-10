#CLASSE QUE REPRESENTA OS DISPOSITIVOS DE ENTRADA E SAÍDA DE DADOS (INPUT OUTPUT SYSTEM) DO IAS#
import webbrowser


class EntradaSaida:
    def inicializar(self):
        print('Dispositivos de Entrada e Saída incializados...')
        webbrowser.open("C:/wamp64/www/UFMA/archias/View/archias.html", new=1)

    def exibirResultado(self):
        print('Exibindo resultado do programa no navegador padrão instalado...')
        webbrowser.open(
            "C:/wamp64/www/UFMA/archias/View/resultado.html", new=1)

    def exibirCaracteristicasComputador(self, quantidadeEnderecosMemoria, quantidadeBitsPalavra):
        print('Este Computador Possui ' +
              str(quantidadeEnderecosMemoria) + ' posições de memória')
        print('Este Computador Possui palavras de ' +
              str(quantidadeBitsPalavra) + ' bits')


## NOTA!! REFLETIR SE VALE A PENA OU NAO PASSAR A ABERTURA DO BROWSER NO METODO INICILIZAR PARA UMA FUNÇÃO MAIS ATRAENTE...