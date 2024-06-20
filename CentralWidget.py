from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QGridLayout, QLineEdit, QRadioButton, QCheckBox, QButtonGroup


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        label_username = QLabel("Benutzername:")
        label_password = QLabel("Kennwort:")
        label_password.setAlignment(Qt.AlignmentFlag.AlignRight)
        label_mac = QLabel("MAC-Adresse:")

        lineedit_username = QLineEdit()
        lineedit_password = QLineEdit()
        lineedit_password.setEchoMode(QLineEdit.EchoMode.Password)

        lineedit_mac = QLineEdit()
        lineedit_mac.setInputMask(">AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#")

        radio_button_IP = QRadioButton("IP-Adresse")
        radio_button_MAC = QRadioButton("MAC-Adresse")

        radio_button_group = QButtonGroup()
        radio_button_group.addButton(radio_button_IP)
        radio_button_group.addButton(radio_button_MAC)

        check_box_no_echo = QCheckBox("Kennwort im Klartext")
        check_box_length = QCheckBox("Mindestlänge des Kennworts")

        layout = QGridLayout()
        layout.addWidget(label_username, 1, 1)
        layout.addWidget(lineedit_username, 1, 2)
        layout.addWidget(label_password, 2, 1)
        layout.addWidget(lineedit_password, 2, 2)
        layout.addWidget(label_mac, 3, 1)
        layout.addWidget(lineedit_mac, 3, 2)
        layout.addWidget(radio_button_IP, 4, 1)
        layout.addWidget(check_box_no_echo, 4, 2)
        layout.addWidget(radio_button_MAC, 5, 1)
        layout.addWidget(check_box_length, 5, 2)

        self.setLayout(layout)
