import time
import snap7


## Ip donde se esta simulando o donde se encuentra la PLC física
IP = "192.168.165.218"
## Rack donde esta dicha PLC
RACK = 0
## Slot donde se encuentra la PLC dentro del rack, por defecto será 2 ya que la 1 queda reservada para la alimentación
SLOT = 2

# DB_NUMBER = 1
## Numero de la DB, dentro de Tia Portal, ej`DB3` 
DB_NUMBER = 3
## Numero de bytes desde donde queremos leer la DB
START_ADDRESS = 0
## Ultimo byte que leeremos en la DB
SIZE = 259

## Llamar a la conexión
plc = snap7.client.Client()
plc.connect(IP, RACK, SLOT)

## Obtener información sobre la CPU
plc_info = plc.get_cpu_info()
print(f'Module Type: {plc_info.ModuleTypeName}')

## Mostrar el estado de la CPU
state = plc.get_cpu_state()
print(f'State:{state}')

## Obtener la DB
db = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE)

## Leer el valor 'String' hasta el byte 256
product_name = db[2:256].decode('UTF-8').strip('\x00')
print(f'PRODUCT NAME: {product_name}')

## Leer el valor 'int'
product_value = int.from_bytes(db[256:258], byteorder='big')
print(f'PRODUCT VALUE: {product_value}')

## Leer el valor 'bool'
product_status = bool(db[258])
print(product_status)

time.sleep(15)