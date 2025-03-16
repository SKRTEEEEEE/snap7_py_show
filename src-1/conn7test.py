import snap7

IP = "192.168.1.133"
# IP = "192.168.1.10"
# IP = "192.168.165.218"
RACK = 0
SLOT = 2

plc = snap7.client.Client()

try:
    print(f"Intentando conectar a {IP} en rack {RACK}, slot {SLOT}...")
    plc.connect(IP, RACK, SLOT)
    print("✅ Conexión exitosa!")
    
    state = plc.get_cpu_state()
    print(f"Estado de la CPU: {state}")

except Exception as e:
    print(f"❌ Error al conectar: {e}")

finally:
    plc.disconnect()
    print("🔌 Conexión cerrada")
