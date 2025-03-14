# Captura de datos con snap7 y pyhton - Conectividad a PLC SIEMENS

## Configuración python
- Debemos tener `python` en nuestra maquina. Para ello podemos ejecutar `python -V` para comprobarlo.
- Debemos tener instalado `pip` en nuestra maquina. Para comprobar-lo podemos ejecutar `python -m pip --version`.
  - En caso de no tenerlo podemos ejecutar `python -m ensurepip --default-pip` para instalar-lo.
- Debemos instalar [`snap7-python`](https://pypi.org/project/python-snap7/) en python, para ello ejecutamos `pip install python-snap7`.
- Debemos tener `snap7` en nuestro sistema. Para ello [descargamos la ultima version](https://sourceforge.net/projects/snap7/files/) y el archivo `snap7.dll` lo ponemos en nuestra carpeta `System32` -> ej `C:\Windows\System32`
### EXTRA - Error conexión
Si tenemos problemas de conexión, muy probablemente se deba al PLCSIM, si hemos configurado todo bien:
- Debemos tener la misma red, osea si nuestra red corre en '192.168.1.190' la PLC debe estar en '192.168.1.[...]'
  - Si esto no funciona:
- Debemos configurar un puente que nos permita conectar-nos a la PLCSIM. Recomiendo [`NetToPLCSim`](https://nettoplcsim.sourceforge.net/).
    
    [Puedes encontrar mas información sobre esto aquí](./err-plssim.md)