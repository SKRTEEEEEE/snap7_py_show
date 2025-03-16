import snap7



def readDB(): 

    # 1. PLC connection definition
    # IP = '192.168.165.218'
    # IP = "192.168.0.1"
    IP = "192.168.1.133"
    RACK = 0
    SLOT = 2

    DB_NUMBER = 3
    START_ADDRESS = 0
    SIZE = 259

    # 1.1 PLC connection via snap7 client module
    plc = snap7.client.Client()
    plc.connect(IP, RACK, SLOT)

    # 2. Read PLC data
    plc_info = plc.get_cpu_info()
    plc_Type = plc_info.ModuleTypeName.decode('UTF-8').strip('\x00')
    #print(f'Module Type: {plc_info.ModuleTypeName}')
    plc_state = plc.get_cpu_state()
    # print(f'State:{plc_state}')

    # 3. Point DB and read data
    db = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE)
    product_name = db[2:256].decode('UTF-8').strip('\x00')
    ## print(f'PRODUCT NAME: {product_name}')
    product_value = int.from_bytes(db[256:258], byteorder='big')
    ## print(f'PRODUCT VALUE: {product_value}')
    product_status = bool(db[258])
    # print(product_status)

    return (plc_Type, plc_state, product_name, product_value, product_status)


if __name__ == '__main__':
    datos = readDB()
    print(datos)