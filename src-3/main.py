from opcua import Client, ua

client_ip = "opc.tcp://192.168.0.1:4840"
node_id_contador_1_resultado = 'ns=3;s="Datos"."Contador1Resultado"' # int in db global
node_id_motor_1_habilitado = 'ns=3;s="Motor1_DB"."Habilitado"' # bool in instance db

def read_input_value(node_id):
    client_node = client.get_node(node_id)  # get node
    client_node_value = client_node.get_value()  # read node value
    print("Value of : " + str(client_node) + ' : ' + str(client_node_value))


def write_value_int(node_id, value):
    client_node = client.get_node(node_id)  # get node
    client_node_value = value
    client_node_dv = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.Int16))
    client_node.set_value(client_node_dv)
    print("Value for write : " + str(client_node) + ' : ' + str(client_node_value))


def write_value_bool(node_id, value):
    client_node = client.get_node(node_id)  # get node
    client_node_value = value
    client_node_dv = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.Boolean))
    client_node.set_value(client_node_dv)
    print("Value for write : " + str(client_node) + ' : ' + str(client_node_value))


if __name__ == "__main__":


    client = Client(client_ip)
    try:
        client.connect()

        root = client.get_root_node()
        print("Objects root node is: ", root)


        read_input_value(node_id_contador_1_resultado)
        read_input_value(node_id_motor_1_habilitado)

        write_value_int(node_id_contador_1_resultado, 100)
        write_value_bool(node_id_motor_1_habilitado, True)

        read_input_value(node_id_contador_1_resultado)
        read_input_value(node_id_motor_1_habilitado)


    finally:
        client.disconnect()