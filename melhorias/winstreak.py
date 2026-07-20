import sys
from rec import recurso
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout
)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

class Janela(QWidget):
    def __init__(self):
        super().__init__()

        self.contador = 0

        self.setWindowTitle("Win-Streak")
        self.resize(350, 150)
        self.setWindowIcon(QIcon(recurso("wins.png")))

        self.label = QLabel("Win-Streak = 0")
        self.label.setAlignment(Qt.AlignCenter)

        self.botao_ganhei = QPushButton("Ganhei")
        self.botao_zerar = QPushButton("Zerei")
        self.botao_sair = QPushButton("Sair")

        self.botao_ganhei.clicked.connect(self.ganhar)
        self.botao_zerar.clicked.connect(self.zerar)
        self.botao_sair.clicked.connect(self.close)

        layout_principal = QVBoxLayout()
        layout_botoes = QHBoxLayout()

        layout_principal.addWidget(self.label)

        layout_botoes.addWidget(self.botao_ganhei)
        layout_botoes.addWidget(self.botao_zerar)
        layout_botoes.addWidget(self.botao_sair)

        layout_principal.addLayout(layout_botoes)

        self.setLayout(layout_principal)

        self.setStyleSheet("""
            QWidget {
                background-color: #202020;
            }

            QLabel {
                color: white;
                font-size: 24px;
                font-weight: bold;
                text-align: center;
            }

            QPushButton {
                background-color: #2d89ef;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 8px;
            }

            QPushButton:hover {
                background-color: #4da3ff;
            }
        """)

    def ganhar(self):
        self.contador += 1
        self.label.setText(f"Win-Streak = {self.contador}")

    def zerar(self):
        self.contador = 0
        self.label.setText("Win-Streak = 0")


app = QApplication(sys.argv)

janela = Janela()
janela.show()

app.exec()