import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile
import readDB


class mainFormReadDB:
    def __init__(self):
        super().__init__()
        # Cargar el archivo .ui
        self.ui = QUiLoader().load(QFile("C:/Users/Laptop/Code/automation/jauz25/snap7_test/main_window.ui"))
        
        # Conectar el botón con la función de lectura
        self.ui.btnRead.clicked.connect(self.read)

    def read(self):
        # Ejecutar la función readDB del módulo readDB
        datos = readDB.readDB()

        # Asignar los valores obtenidos a los campos del formulario
        cpuType = datos[0]
        cpuStatus = datos[1]
        name = datos[2]
        value = datos[3]
        status = datos[4]

        # Mostrar los datos de la CPU
        self.ui.txtCpuType.setText(f"{cpuType}")

        # Cambiar el color del led en función del estado de la CPU
        if cpuStatus == 'S7CpuStatusRun':
            self.ui.ledCpuStatus.setStyleSheet(u"background-color: rgb(0, 255, 0);border-radius:15px;")
        else:
            self.ui.ledCpuStatus.setStyleSheet(u"background-color: rgb(255, 0, 0);border-radius:15px;")

        # Mostrar los datos de DB
        self.ui.txtName.setText(f"{name}")
        self.ui.lcdValue.setProperty("intValue", value)

        # Cambiar el color del led en función del estado del DB
        if status:
            self.ui.ledStatus.setStyleSheet(u"background-color: rgb(0, 255, 0);border-radius:30px;")
        else:
            self.ui.ledStatus.setStyleSheet(u"background-color: rgb(255, 0, 0);border-radius:30px;")


if __name__ == "__main__":
    # Crear la aplicación y la instancia de la ventana principal
    app = QApplication(sys.argv)
    myapp = mainFormReadDB()
    
    # Mostrar la UI
    myapp.ui.show()
    
    # Ejecutar el bucle de eventos de la aplicación
    sys.exit(app.exec())
