# Error conexión a PLC SIM

## Ping sin respuesta

Si estás usando **PLCSIM** y el **ping falla**, el problema es que el PLC SIMULADO no está accesible desde tu red. Aquí hay algunas soluciones específicas para esto:  

---

### 🔍 **1. Verifica que el Adaptador de Red Virtual de PLCSIM esté activo**  
PLCSIM Advanced crea una **interfaz de red virtual** para la simulación. Verifica en **Panel de Control → Centro de redes y recursos compartidos → Cambiar configuración del adaptador** si hay un adaptador de red con un nombre tipo **"PLCSIM Virtual Adapter"**.  

✔ **Si el adaptador está deshabilitado**, actívalo.  
✔ **Si no aparece**, reinstala PLCSIM y habilita la opción de red virtual.  


## s7 PLCSIM vs PLCSIM Advanced
Si estás usando **S7-PLCSIM (el estándar, no Advanced)** y el **ping falla**, el problema es que **PLCSIM estándar no expone la red al sistema operativo**. Esto significa que **Snap7 no puede comunicarse directamente con el PLC simulado** porque **S7-PLCSIM no emula una interfaz de red real**.  

### 🚨 **Solución: Usar NetToPLCSim**  
Para hacer que Snap7 pueda comunicarse con **S7-PLCSIM**, necesitas un puente de red. La mejor opción es usar **NetToPLCSim**, que permite exponer el PLC simulado a la red.  

#### ✅ **Pasos para configurar NetToPLCSim**  
1️⃣ **Descarga NetToPLCSim**  
   - Puedes encontrarlo aquí: [https://nettoplcsim.sourceforge.io/](https://nettoplcsim.sourceforge.io/)  

2️⃣ **Ejecuta NetToPLCSim como Administrador**  
   - Abre el programa después de instalarlo.  
   - Debería detectar automáticamente tu PLC simulado.  

3️⃣ **Configura la IP del PLC virtual**  
   - En **"Local IP Address"**, elige la IP que quieres usar (ejemplo: `192.168.1.10`).  
   - En **"PLCSIM Rack / Slot"**, pon `0` y `2` si es un **S7-300** o `0` y `1` si es un **S7-1200/S7-1500**.  
   - Haz clic en **"Start Server"** para habilitar la conexión.  

4️⃣ **Prueba el ping**  
   - Ejecuta en la terminal:  
     ```bash
     ping 192.168.1.10
     ```
   - Si ahora responde, significa que **ya tienes acceso al PLC desde Snap7**.  

---

### 🔄 **Modifica tu código de Snap7**  
Ahora en tu código, asegúrate de conectar a la IP que configuraste en NetToPLCSim:

```python
IP = "192.168.1.10"  # Debe coincidir con la configurada en NetToPLCSim
plc.connect(IP, 0, 2)  # Para S7-300/S7-400
```

Para **S7-1200/S7-1500**, usa:

```python
plc.connect(IP, 0, 1)
```

---

### 🎯 **Resumen**
- **S7-PLCSIM (estándar) no permite comunicación TCP/IP por defecto.**  
- **NetToPLCSim** soluciona esto al actuar como un puente entre PLCSIM y la red.  
- **Una vez configurado, Snap7 puede conectarse normalmente.**  

