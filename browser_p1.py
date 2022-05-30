
from PyQt5.QtWidgets import *
import sys #Importar as funções do sistema operacional
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        #Invoco o construtor da classe pai
        super(JanelaPrincipal, self).__init__()
        self.showMaximized() #Aprese0nta a tela maximizada

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://www.google.com.br'))
        self.setCentralWidget(self.browser)

        barra_de_nav = QToolBar() #Cria uma barra de navegação
        self.addToolBar(barra_de_nav) #Adicionar a barra de navegação
        #É criado o botão de voltar
        botao_de_voltar = QAction('< Voltar', self)
        #É vinculado a ação de voltar a página ao botão
        botao_de_voltar.triggered.connect(self.browser.back)
        #Adição do botão na barra de navegação
        barra_de_nav.addAction(botao_de_voltar)

        botao_de_avancar = QAction('> Avançar', self)
        botao_de_avancar.triggered.connect(self.browser.forward)
        barra_de_nav.addAction(botao_de_avancar)

        botao_recarregar = QAction('Recarregar a Página', self)
        botao_recarregar.triggered.connect(self.browser.reload)
        barra_de_nav.addAction(botao_recarregar)

        botao_pag_inicial = QAction('Página Inicial', self)
        botao_pag_inicial.triggered.connect(self.pagina_inicial)
        barra_de_nav.addAction(botao_pag_inicial)

        botao_interromper = QAction('Interromper Carregamento', self)
        botao_interromper.triggered.connect(self.browser.stop)
        barra_de_nav.addAction(botao_interromper)

    def pagina_inicial(self):
        self.browser.setUrl(QUrl('http://www.google.com.br'))

aplicacao = QApplication(sys.argv)
QApplication.setApplicationName("Web Browser")
janela = JanelaPrincipal()
aplicacao.exec_()   