<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

# Conectividad a PLC SIEMENS con python
<a href="https://github.com/SKRTEEEEEE">
<div align="center">
  <img  src="https://github.com/SKRTEEEEEE/SKRTEEEEEE/blob/main/resources/img/grid-snake.svg"
       alt="snake" />
</div>
</a>


## Información  
Código de muestra de conectividad a PLC SIEMENS con Python y [`snap7-python`](https://pypi.org/project/python-snap7/), utilizando la conectividad de **Snap7**.  

El proyecto permite la lectura y escritura de datos en un PLC Siemens a través de una conexión TCP/IP, facilitando la interacción con bloques de datos (DB), entradas, salidas y marcas del autómata.  

Incluye ejemplos prácticos para:  
- Establecer conexión con un PLC S7-300/400/1200/1500.  
- Leer y escribir valores en memoria.  
- Manejar estructuras de datos desde Python.  
- Implementar pruebas básicas de comunicación.  

Este código es útil para aplicaciones de monitoreo, control remoto y pruebas en entornos industriales. 🚀  

### 🔹 Requisitos para usar Snap7  
1. **El PLC debe soportar comunicaciones mediante ISO on TCP (RFC1006)**.  
   - Esto es común en los **S7-300, S7-400, S7-1200 y S7-1500**.  
2. **El PLC debe tener configurado un puerto Ethernet con accesos habilitados**.  
   - Normalmente, el puerto estándar es **102**.  
3. **El firewall y la red deben permitir el tráfico TCP/IP** entre el PLC y la PC.  

## [Recursos](https://github.com/SKRTEEEEEE/markdowns)
### Guía (Como usar/contenido)


#### Captura de datos con snap7 y pyhton
_para esta parte utilizaremos [`src-1`](./src-1/)_
##### Configuración python
- Debemos tener `python` en nuestra maquina. Para ello podemos ejecutar `python -V` para comprobarlo.
- Debemos tener instalado `pip` en nuestra maquina. Para comprobar-lo podemos ejecutar `python -m pip --version`.
  - En caso de no tenerlo podemos ejecutar `python -m ensurepip --default-pip` para instalar-lo.
- Debemos instalar [`snap7-python`](https://pypi.org/project/python-snap7/) en python, para ello ejecutamos `pip install python-snap7`.
- Debemos tener `snap7` en nuestro sistema. Para ello [descargamos la ultima version](https://sourceforge.net/projects/snap7/files/) y el archivo `snap7.dll` lo ponemos en nuestra carpeta `System32` -> ej `C:\Windows\System32`
###### EXTRA -> conexión
Si tenemos problemas de conexión, muy probablemente se deba al PLCSIM, si hemos configurado todo bien:
- Debemos tener la misma red, osea si nuestra red corre en '192.168.1.190' la PLC debe estar en '192.168.1.[...]'
- Debemos también configurar un puente que nos permita conectar-nos a la PLCSIM. Recomiendo [`NetToPLCSim`](https://nettoplcsim.sourceforge.net/).
    
    [Puedes encontrar mas información sobre esto aquí](./err-plssim.md)
##### Configuración PLC
- Debemos configurar una PLC en nuestro Tia Portal
- Quitar todas las restricciones de comunicación
- _Se recomienda usar la gama 300, ya que contiene menos restricciones_
- Crear una base de datos, con los valores que queremos leer.
- Compilar, cargar la PLC y conectar-se
##### Captura de datos en python
- Ejecutar el script [`snap7test`](./src-1/snap7test.py)
- Podemos cambiar el valor de los bytes desde Tia Portal y observar como al ejecutar de nuevo el script anterior, nos devuelve los datos actualizados
- _Si obtienes un error de conexión TCP, [observa esta sección](#extra---error-conexión)_

#### Formularios SCADA y HMI
_para esta parte utilizaremos [`src-1`](./src-1/)_
##### Configuración [entorno virtual python](./entorno-virtual.md)
- Instalamos nuestro entorno virtual: `pip install virtualenv`
  - Si nos falla podemos probar con permisos de usuario: `pip install --user --upgrade --force-reinstall virtualenv`
- Crear entorno virtual: `python -m venv <nombre_deseado>` -> `python -m venv virtual`
- [*Activamos dicho entorno](./entorno-virtual.md#uso-con-distintas-terminales): `source virtual/Scripts/activate`
- Instalamos `PySide2` en nuestro entorno: `pip install PySide2`
  - Si estamos utilizando Python < 3.9, podemos utilizar alternativas como `PySide6`: `pip install PySide6`
- Abrimos `Qt designer`, para ello, debemos ubicarnos en la carpeta donde hemos creado nuestro virtual(raíz), y en el caso de instalar `PySide6`: `virtual/lib/site-packages/PySide6/designer`
##### Ejecución y utilización del entorno virtual
- Ejecutamos nuestra PLC y configuramos la IP de [nuestro archivo que leerá la DB](./src-1/readDB.py) con la IP utilizada.
- Nos ubicamos en nuestra ruta src, si tenemos, para ejecutar nuestro archivo main: `python main.py`
  - Recuerda que debes tener instaladas las dependencias, y tener el entorno configurado si has utilizado un entorno virtual.

#### Lectura y escritura de bits en db sin OPC
_para esta parte utilizaremos [`src-2`](./src-2/)_
##### Configuración
Para esta parte, utilizaremos la misma configuración que en el apartado anterior, [Formularios SCADA y HMI](#formularios-scada-y-hmi).
##### Ejecución
- Ejecutamos nuestra PLC y configuramos la IP de [nuestro archivo que leerá la DB](./src-2/DB.py) con la IP utilizada.
- Nos ubicamos en nuestra ruta src, si tenemos, para ejecutar nuestro archivo main: `python main.py`
##### Uso
- 'starter' -> variable/bit en nuestra DB de la PLC, 258.0
- 'offset' -> variable/bit en nuestra DB de la PLC, 258.1
Este programa de nuestro código de ejemplo consiste en una 'starter', que se inicializa en FALSE. Al cambiar a TRUE (forzado desde PLC/Tia Portal), cuando ejecutemos un bucle de nuestro código (click al botón `READ DATA` de nuestra Scada/HMI), si 'starter' es TRUE, seteamos 'offset' al valor contrario, y se muestra por pantalla.

## Contacto
### [Pagina web del desarrollador](https://profile-skrt.vercel.app)
### [Envíame un mensaje](mailto:adanreh.m@gmail.com)
## Agradecimientos
### [MrDabit](https://github.com/MrDabit)
## Contribuciones y Problemas

Si encuentras problemas o deseas contribuir al proyecto, por favor, crea un issue en el repositorio.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

