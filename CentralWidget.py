from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QTextBrowser, QLineEdit, QPushButton, QTimeEdit, QLCDNumber, \
    QRadioButton


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        grid_layout = QGridLayout()

        label1 = QLabel("Blind in €")
        grid_layout.addWidget(label1, 1, 1)

        label2 = QLabel("Raise-Time")
        grid_layout.addWidget(label2, 2, 1)

        label_3 = QLabel("Raise in %")
        grid_layout.addWidget(label_3, 3, 1)

        label_4= QLabel("Blind in €")
        grid_layout.addWidget(label_4, 4, 1)

        self.line_edit_1 = QLineEdit("50")
        grid_layout.addWidget(self.line_edit_1, 1, 2)

        self.line_edit_2 = QTimeEdit()
        grid_layout.addWidget(self.line_edit_2, 2, 2)

        self.line_edit_3 = QLineEdit("15.3%")
        grid_layout.addWidget(self.line_edit_3, 3, 2)

        self.line_edit_4 = QLineEdit("50")
        grid_layout.addWidget(self.line_edit_4, 4, 2)

        self.push_button = QPushButton("Start/Stopp")
        grid_layout.addWidget(self.push_button, 1, 3)

        lcd_timer = QLCDNumber()
        lcd_timer.display(0)
        grid_layout.addWidget(lcd_timer, 2, 3)

        self.radio_button = QRadioButton("Raise in %")
        grid_layout.addWidget(self.radio_button, 3, 3)

        self.radio_button_2 = QRadioButton("Raise in €")
        grid_layout.addWidget(self.radio_button_2, 4, 3)

        self.text_browser = QTextBrowser()
        grid_layout.addWidget(self.text_browser, 5, 1, 1, 4)

        self.setLayout(grid_layout)
