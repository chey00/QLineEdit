from PyQt6.QtWidgets import QWidget, QLineEdit, QTextBrowser, QGridLayout, QPushButton, QLabel


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.__lineEditUsername = QLineEdit(self)
        self.__lineEditUsername.setInputMask(4 * "A" + 6 * "a")

        self.__lineEditPassword = QLineEdit(self)
        self.__lineEditPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.__pushButtonCopy = QPushButton("Copy input", self)
        self.__pushButtonCopy.released.connect(self.copyToTextbrowser)

        self.__pushButtonClear = QPushButton("Clear output", self)
        self.__pushButtonClear.clicked.connect(self.clearTextbrowser)

        self.__textBrowser = QTextBrowser(self)

        gridLayout = QGridLayout()
        gridLayout.addWidget(QLabel("Benutzername"), 0, 0)
        gridLayout.addWidget(self.__lineEditUsername, 0, 1)
        gridLayout.addWidget(QLabel("Passwort"), 1, 0)
        gridLayout.addWidget(self.__lineEditPassword, 1, 1)
        gridLayout.addWidget(self.__pushButtonCopy, 2, 0)
        gridLayout.addWidget(self.__pushButtonClear, 2, 1)
        gridLayout.addWidget(self.__textBrowser, 3, 0, 1, 0)
        self.setLayout(gridLayout)

    def copyToTextbrowser(self):
        username = self.__lineEditUsername.text()
        password = self.__lineEditPassword.text()

        self.__textBrowser.append("username: " + username)
        self.__textBrowser.append("password: " + password)

    def clearTextbrowser(self):
        self.__textBrowser.clear()
