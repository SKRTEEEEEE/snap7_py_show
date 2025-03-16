import snap7


IP = "192.168.1.133"
RACK = 0
SLOT = 2

DB_NUMBER = 3
START_ADDRESS = 0
SIZE = 259

# WRITE_DB_ADDRESS = 258
# SIZE_WRITE = 1

# 1.1 PLC connection via snap7 client module
plc = snap7.client.Client()
plc.connect(IP, RACK, SLOT)

def readDB(byte, bit):
    db = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE)
    status = snap7.util.get_bool(db, byte, bit)
    return (status)

# def writeDB(byte, bit, bitvalue):
#     db = plc.db_read(DB_NUMBER, WRITE_DB_ADDRESS, SIZE_WRITE)
#     snap7.util.set_bool(db, byte, bit, bitvalue)
#     plc.db_write(DB_NUMBER, START_ADDRESS, db)

def writeDB(byte, bit, bitvalue):
    # Leer SOLO el byte específico que vamos a modificar
    db = plc.db_read(DB_NUMBER, byte, 1)  # Leer 1 byte desde la posición del byte objetivo
    # db = plc.db_read(DB_NUMBER, WRITE_DB_ADDRESS, SIZE_WRITE)  # Aunque esto funciona, es mejor practica la línea anterior
    
    # Modificar el bit específico
    snap7.util.set_bool(db, 0, bit, bitvalue)  # Usar offset 0 porque leímos solo 1 byte
    
    # Escribir de vuelta en la MISMA posición del byte
    plc.db_write(DB_NUMBER, byte, db)
