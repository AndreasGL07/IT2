from PySide6.QtWidgets import QMainWindow, QPushButton

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__(self)
        self.setWindowTitle("Button Holder app")
        button = QPushButton("Press me!")
        # Set our button as the sentral widget
        self.setCentralWidget(button)