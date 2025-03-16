# Conectividad a PLC SIEMENS
## Captura de datos con snap7 y pyhton
### Configuración python
- Debemos tener `python` en nuestra maquina. Para ello podemos ejecutar `python -V` para comprobarlo.
- Debemos tener instalado `pip` en nuestra maquina. Para comprobar-lo podemos ejecutar `python -m pip --version`.
  - En caso de no tenerlo podemos ejecutar `python -m ensurepip --default-pip` para instalar-lo.
- Debemos instalar [`snap7-python`](https://pypi.org/project/python-snap7/) en python, para ello ejecutamos `pip install python-snap7`.
- Debemos tener `snap7` en nuestro sistema. Para ello [descargamos la ultima version](https://sourceforge.net/projects/snap7/files/) y el archivo `snap7.dll` lo ponemos en nuestra carpeta `System32` -> ej `C:\Windows\System32`
#### EXTRA - Error conexión
Si tenemos problemas de conexión, muy probablemente se deba al PLCSIM, si hemos configurado todo bien:
- Debemos tener la misma red, osea si nuestra red corre en '192.168.1.190' la PLC debe estar en '192.168.1.[...]'
  - Si esto no funciona:
- Debemos configurar un puente que nos permita conectar-nos a la PLCSIM. Recomiendo [`NetToPLCSim`](https://nettoplcsim.sourceforge.net/).
    
    [Puedes encontrar mas información sobre esto aquí](./err-plssim.md)
### Configuración PLC
- Debemos configurar una PLC en nuestro Tia Portal
- Quitar todas las restricciones de comunicación
- _Se recomienda usar la gama 300, ya que contiene menos restricciones_
- Crear una base de datos, con los valores que queremos leer.
- Compilar, cargar la PLC y conectar-se
### Captura de datos en python
- Ejecutar el script [`snap7test`](./src/snap7test.py)
- Podemos cambiar el valor de los bytes desde Tia Portal y observar como al ejecutar de nuevo el script anterior, nos devuelve los datos actualizados

## Formularios SCADA y HMI
### Configuración [entorno virtual python](./entorno-virtual.md)
- Instalamos nuestro entorno virtual: `pip install virtualenv`
  - Si nos falla podemos probar con permisos de usuario: `pip install --user --upgrade --force-reinstall virtualenv`
- Crear entorno virtual: `python -m venv <nombre_deseado>` -> `python -m venv virtual`
- [*Activamos dicho entorno](./entorno-virtual.md#uso-con-distintas-terminales): `source virtual/Scripts/activate`
- Instalamos `PySide2` en nuestro entorno: `pip install PySide2`
  - Si estamos utilizando Python < 3.9, podemos utilizar alternativas como `PySide6`: `pip install PySide6`
- Abrimos `Qt designer`, para ello, debemos ubicarnos en la carpeta donde hemos creado nuestro virtual(raíz), en el caso de instalar `PySide6`: `virtual/lib/site-packages/PySide6/designer`
