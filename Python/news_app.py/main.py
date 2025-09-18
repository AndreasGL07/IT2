
#The sys module is responsible for processing command line arguments
import sys
from PySide6.QtWidgets import QApplication, QPushButton

def button_clicked():
    print("You clicked the button")

app = QApplication(sys.argv)
button = QPushButton("Start")
button.setCheckable(True) #Makes the button checkable. It's unchecked by default. Further clicks toggle between checked and unchecked states


#clicked is a signal for QPushButton. It's emitted when you click the button. You can wire a slot to the signal using the syntax below
button.clicked.connect(button_clicked) 

button.show()
app.exec()