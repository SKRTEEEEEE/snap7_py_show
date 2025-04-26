<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

# Conectividad a PLC con python
<a href="https://github.com/SKRTEEEEEE">
<div align="center">
  <img  src="https://github.com/SKRTEEEEEE/SKRTEEEEEE/blob/main/resources/img/grid-snake.svg"
       alt="snake" />
</div>
</a>


## Información  
Código de muestra de conectividad a PLC con Python. Ejemplos realizados con PLCs SIEMENS, Tia Portal y:
- [`snap7-python`](https://pypi.org/project/python-snap7/), utilizando la conectividad **Snap7**.
- [`python-opcua`](https://github.com/FreeOpcUa/python-opcua), utilizando la conectividad **OPC UA**.  

El proyecto permite la lectura y escritura de datos, como ejemplo en un PLC Siemens, a través de conexión TCP/IP, facilitando la interacción con bloques de datos (DB), entradas, salidas, marcas del autómata...

Incluye ejemplos prácticos para:  
- Establecer conexión con un PLC o similar.
- Leer y escribir valores en memoria.  
- Manejar estructuras de datos desde Python.  
- Implementar pruebas básicas de comunicación.  

Este código es útil para aplicaciones de monitoreo, control remoto y pruebas en entornos industriales. 🚀  

### 🔹 Requisitos para usar Snap7  
1. **El PLC debe soportar comunicaciones mediante ISO on TCP (RFC1006)**.  
   - Esto es común en los **S7-300, S7-400, S7-1200 y S7-1500**. Al igual que en otros muchos dispositivos como Arduino.
2. **El PLC debe tener configurado un puerto Ethernet con accesos habilitados**.  
   - El puerto estándar es **102**.  
3. **El firewall y la red deben permitir el tráfico TCP/IP** entre el PLC y la PC.  
### 🔹 Requisitos para usar OPC UA  
1. **El PLC, servidor o dispositivo debe soportar el protocolo OPC UA nativamente** o a través de un gateway o servidor externo.  
   - Muchos PLCs modernos como **S7-1200, S7-1500**, **Beckhoff**, **Wago**, entre otros, ya incluyen servidores OPC UA.  
2. **El servidor OPC UA debe estar configurado y activo**, con los endpoints disponibles para clientes.  
   - Normalmente se define un **Endpoint URL** tipo: `opc.tcp://<ip-servidor>:<puerto>`.  
   - El puerto más habitual es **4840**, pero puede cambiarse.  
3. **El cliente OPC UA debe soportar los perfiles de seguridad requeridos** si el servidor tiene habilitada la autenticación o el cifrado.  
   - Esto incluye certificados, usuarios/contraseñas, o incluso sesiones anónimas si está permitido.  
4. **La red debe permitir la comunicación TCP/IP entre cliente y servidor**.  
   - Revisa también que no existan bloqueos por firewall en el puerto OPC UA configurado.
## [Recursos](https://github.com/SKRTEEEEEE/markdowns)
### Guía snap7 (Como usar/contenido)
#### Configuración
##### Configuración python base
- Debemos tener `python` en nuestra maquina. Para ello podemos ejecutar `python -V` para comprobarlo.
- Debemos tener instalado `pip` en nuestra maquina. Para comprobar-lo podemos ejecutar `python -m pip --version`.
  - En caso de no tenerlo podemos ejecutar `python -m ensurepip --default-pip` para instalar-lo.
##### Configuración librería python snap7
- Debemos instalar [`snap7-python`](https://pypi.org/project/python-snap7/) en python, para ello ejecutamos `pip install python-snap7`.
##### Simulación/Ejecución
- Debemos tener `snap7` en nuestro sistema. Para ello [descargamos la ultima version](https://sourceforge.net/projects/snap7/files/) y el archivo `snap7.dll` lo ponemos en nuestra carpeta `System32` -> ej `C:\Windows\System32`
Si tenemos problemas de conexión, muy probablemente se deba al PLCSIM (en el caso de simulación), si hemos configurado todo bien:
- Debemos tener la misma red, osea si nuestra red corre en '192.168.1.190' la PLC debe estar en '192.168.1.[...]'
- Debemos también configurar un puente que nos permita conectar-nos a la PLCSIM. Recomiendo [`NetToPLCSim`](https://nettoplcsim.sourceforge.net/).
    
    [Puedes encontrar mas información sobre esto aquí](./err-plssim.md)
##### Configuración PLC
[*Puedes utilizar la siguiente configuración de muestra para Tia Portal*](./snap7-tia.7z)
- Debemos configurar una PLC en nuestro Tia Portal
- Quitar todas las restricciones de comunicación
- _Se recomienda usar la gama 300, ya que contiene menos restricciones_
- Crear una base de datos, con los valores que queremos leer.
- Compilar, cargar la PLC y conectar-se
#### Captura de datos en python
_ejemplo de esta parte en [`src-1`](./src-1/)_
- Ejecutar el script [`snap7test`](./src-1/snap7test.py)
- Podemos cambiar el valor de los bytes desde Tia Portal y observar como al ejecutar de nuevo el script anterior, nos devuelve los datos actualizados
- _Si obtienes un error de conexión TCP, [observa esta sección](#extra---error-conexión)_

#### Formularios SCADA y HMI
_ejemplo de esta parte en [`src-1`](./src-1/)_
##### Configuración [entorno virtual python](./entorno-virtual.md)
- Instalamos la librería para entorno virtual si no la tenemos en nuestra máquina: `pip install virtualenv`
  - Si nos falla podemos probar con permisos de usuario: `pip install --user --upgrade --force-reinstall virtualenv`
- Crear entorno virtual: `python -m venv <nombre_deseado>` -> `python -m venv virtual`
- [*Activamos dicho entorno](./entorno-virtual.md#uso-con-distintas-terminales): `source <nombre_entorno>/Scripts/activate` -> `source virtual/Scripts/activate`
- Instalamos `PySide2` en nuestro entorno: `pip install PySide2`
  - Si estamos utilizando Python < 3.9, podemos utilizar alternativas como `PySide6`: `pip install PySide6`
- Abrimos `Qt designer`, para ello, debemos ubicarnos en la carpeta donde hemos creado nuestro virtual(raíz), y en el caso de instalar `PySide6`: `virtual/lib/site-packages/PySide6/designer`
##### Ejecución y utilización del entorno virtual
- Ejecutamos nuestra PLC y configuramos la IP de [nuestro archivo que leerá la DB](./src-1/readDB.py) con la IP utilizada.
- Nos ubicamos en nuestra ruta src, si tenemos, para ejecutar nuestro archivo main: `python main.py`
  - Recuerda que debes tener instaladas las dependencias, y tener el entorno configurado si has utilizado un entorno virtual.

#### Lectura y escritura de bits en db
_ejemplo de esta parte en [`src-2`](./src-2/)_
##### Configuración
Para esta parte, utilizaremos la misma configuración que en el apartado anterior, [Formularios SCADA y HMI](#formularios-scada-y-hmi).
##### Ejecución
- Ejecutamos nuestra PLC y configuramos la IP de [nuestro archivo que leerá la DB](./src-2/DB.py) con la IP utilizada.
- Nos ubicamos en nuestra ruta src, si tenemos, para ejecutar nuestro archivo main: `python main.py`
##### Uso
- 'starter' -> variable/bit en nuestra DB de la PLC, 258.0
- 'offset' -> variable/bit en nuestra DB de la PLC, 258.1
Este programa de nuestro código de ejemplo consiste en una 'starter', que se inicializa en FALSE. Al cambiar a TRUE (forzado desde PLC/Tia Portal), cuando ejecutemos un bucle de nuestro código (click al botón `READ DATA` de nuestra Scada/HMI), si 'starter' es TRUE, seteamos 'offset' al valor contrario, y se muestra por pantalla.

### Guía OPC UA
#### Configuración
- Necesitamos [tener python e pip instalados en nuestra maquina](#configuración-python-base).
##### Entorno virtual
- Instalamos la librería para entorno virtual si no la tenemos en nuestra máquina: `pip install virtualenv`
  - Si nos falla podemos probar con permisos de usuario: `pip install --user --upgrade --force-reinstall virtualenv`
- Crear entorno virtual: `python -m venv <nombre_deseado>` -> `python -m venv opcua_virtual`
- [*Activamos dicho entorno](./entorno-virtual.md#uso-con-distintas-terminales): `source <nombre_entorno>/Scripts/activate` -> `source opcua_virtual/Scripts/activate`
- Instalamos [`opcua-client`](https://github.com/FreeOpcUa/opcua-client-gui) en nuestro entorno: `pip install opcua-client`
- Instalamos [`python-opcua`](https://github.com/FreeOpcUa/python-opcua) en nuestro entorno: `pip install opcua`
##### Simulación/Ejecución
Para simular o ejecutar OPC UA con Tia Portal, deberemos tener al menos una PLC física con compatibilidad OPC UA para ejecutarlo o PLCSIM ADVANCED para simular-lo desde nuestra máquina. 
##### Configuración PLC
[*Puedes utilizar la siguiente configuración de muestra para Tia Portal*](./opcua-tia.7z)
- Debemos configurar una PLC con OPC UA en nuestro Tia Portal, se recomienda s1500
- Quitar todas las restricciones de comunicación
- Crear una base de datos, con los valores que queremos leer.
- Habilitar un servidor OPC UA
  - La forma mas sencilla, es ir a las `propiedades` de nuestra PLC -> `OPC UA` -> `Server` -> buscamos el checkbox `Activate OPC UA server` y lo activamos. Entonces nos permite exponer la IP deseada a traves de OPC UA.
- Compilar y cargar la PLC. Recuerda que si estas simulando, solo podrás hacer-lo utilizando PLCSIM ADVANCED, seleccionando una conexión `PLCSIM Virtual Ethernet Adapter`.
#### Captura de datos con [`opcua-client`](https://github.com/FreeOpcUa/opcua-client-gui)
- Abrimos `opcua-client`, para ello, debemos tener activado el entorno virtual donde hemos instalado la librería y ejecutar: `opcua-client`
- Una vez abierto el programa, podemos introducir la IP que estemos exponiendo a traves de OPC UA y seleccionar el botón de `conectar`.
- Esto nos permite leer los datos actuales en el momento de la conexión, si queremos leer un estado que ha cambiado debemos hacer click en `Refresh`
#### Captura de datos y escritura con python
_ejemplo de esta parte en [`src-3`](./src-3/)_
- Ejecutamos nuestra PLC y configuramos la IP donde se ejecuta el servidor OPC UA, al igual que los NodeId de las variables que vayamos a leer en el archivo [main.py](./src-3/main.py).
- Nos ubicamos en nuestra ruta src, para ejecutar el archivo main: `python main.py`
## Contacto
### [Pagina web del desarrollador](https://profile-skrt.vercel.app)
### [Envíame un mensaje](mailto:adanreh.m@gmail.com)
## Agradecimientos
### [MrDabit](https://github.com/MrDabit)
### [Mareh07](https://github.com/Mareh07)
## Contribuciones y Problemas

Si encuentras problemas o deseas contribuir al proyecto, por favor, crea un issue en el repositorio.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

