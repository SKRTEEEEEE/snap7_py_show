import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile
import DB

class mainFormReadDB:
    def __init__(self):
        super().__init__()
        # Cargar el archivo .ui
        self.ui = QUiLoader().load(QFile("C:/Users/Laptop/Code/automation/jauz25/snap7_test/main_window.ui"))
        
        # Conectar el botón con la función de lectura
        self.ui.btnRead.clicked.connect(self.read)

    def read(self):
        try:
            # Leer datos de la CPU
            cpu_info = DB.plc.get_cpu_info()
            plc_Type = cpu_info.ModuleTypeName.decode('UTF-8').strip('\x00')
            plc_state = DB.plc.get_cpu_state()

            # Leer datos de la DB
            db = DB.plc.db_read(DB.DB_NUMBER, DB.START_ADDRESS, DB.SIZE)
            product_name = db[2:256].decode('UTF-8').strip('\x00')
            product_value = int.from_bytes(db[256:258], byteorder='big')
            
            # Leer estado de los bits específicos
            starter = DB.readDB(258, 0)  # Bit 258.0 (starter)
            offset = DB.readDB(258, 1)   # Bit 258.1 (offset)

            # Mostrar datos de la CPU
            self.ui.txtCpuType.setText(plc_Type)
            self.ui.ledCpuStatus.setStyleSheet(
                u"background-color: rgb(0, 255, 0);border-radius:15px;" 
                if plc_state == 'S7CpuStatusRun' 
                else u"background-color: rgb(255, 0, 0);border-radius:15px;"
            )

            # Mostrar datos del producto
            self.ui.txtName.setText(product_name)
            self.ui.lcdValue.display(product_value)


            # Trabajar a partir de aquí
            print(f"Starter: {starter}")
            print(f"Offset: {offset}")
           # Modificar el estado de offset según starter
            if starter:
                DB.writeDB(258, 1, True)  # Escribir bit 1 (258.1)
            else:
                DB.writeDB(258, 1, False)

            # Forzar nueva lectura del offset después de la escritura
            offset = DB.readDB(258, 1)  # Nueva lectura actualizada

            # Actualizar UI con el nuevo valor
            self.ui.ledStatus.setStyleSheet(
                u"background-color: rgb(0, 255, 0);border-radius:30px;" 
                if offset 
                else u"background-color: rgb(255, 0, 0);border-radius:30px;"
            )

        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = mainFormReadDB()
    myapp.ui.show()
    sys.exit(app.exec())
