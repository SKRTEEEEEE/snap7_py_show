# Entorno virtual
## ¿Qué es un entorno virtual?  

Un **entorno virtual** es un espacio aislado donde se pueden instalar paquetes de Python sin afectar la configuración global del sistema. Esto es útil para:  

- Mantener versiones específicas de dependencias para cada proyecto.  
- Evitar conflictos con otros entornos de desarrollo.  
- Facilitar la portabilidad del proyecto.  

## Consideraciones al configurar un entorno virtual

Al configurar un entorno virtual en un proyecto de Python, es importante tener en cuenta varios aspectos para asegurar la portabilidad y el buen manejo del código, especialmente si vas a trabajar con herramientas de control de versiones como GitHub. Aquí te presentamos algunas recomendaciones clave:

### **1. Ubicación del entorno virtual**  

El entorno virtual debe estar ubicado en un lugar que facilite su configuración sin interferir con el resto del proyecto. Sin embargo, una de las decisiones más importantes es si debes incluir el entorno virtual dentro de la carpeta del proyecto o fuera de ella.

- **Entorno virtual dentro del proyecto**:  
  Algunas personas optan por crear el entorno virtual dentro de la carpeta del proyecto para mantener todo en un solo lugar. Sin embargo, esto no es recomendable cuando se trabaja con repositorios Git, ya que puede aumentar el tamaño del repositorio innecesariamente y generar conflictos con otros colaboradores.

- **Entorno virtual fuera del proyecto**:  
  La mejor práctica generalmente es crear el entorno virtual fuera de la carpeta del proyecto o en un directorio específico (por ejemplo, una carpeta llamada `envs` a nivel superior). Esto asegura que el entorno virtual no sea parte del código fuente del proyecto y evita incluir archivos generados automáticamente en el repositorio.  

### **2. Ignorar el entorno virtual en Git**

En casi todos los casos, **el entorno virtual no debe ser incluido en el repositorio Git**. Puedes hacerlo agregando la carpeta donde se encuentra el entorno virtual al archivo `.gitignore` para que Git ignore esos archivos. Esto es especialmente importante para evitar que el entorno virtual, que puede ser grande y específico para tu máquina, se suba al repositorio.

Ejemplo de un archivo `.gitignore` para Python:
```gitignore
# Ignorar entorno virtual
venv/
env/
```

Con esto, garantizas que el entorno virtual no se suba a GitHub, y cada colaborador puede crear su propio entorno virtual de manera local.

### **3. Reproducibilidad del entorno**  

Aunque no incluyas el entorno virtual en Git, es esencial documentar las dependencias del proyecto para que otros desarrolladores puedan instalar las mismas versiones de las bibliotecas. Esto se hace mediante el archivo `requirements.txt` (si usas `pip`).

Para generar un archivo `requirements.txt` con las dependencias de tu entorno virtual, usa:
```bash
pip freeze > requirements.txt
```

Luego, cualquier colaborador puede instalar las dependencias ejecutando:
```bash
pip install -r requirements.txt
```

Alternativamente, si trabajas con un entorno más moderno, podrías usar `pipenv` o `poetry`, que también gestionan dependencias y el entorno virtual de manera más sofisticada.


## Uso con distintas terminales
### Git bash
#### 🐧 **Ejecución en Git Bash**
Git Bash no usa scripts de PowerShell (`.ps1`), sino archivos `activate` de Bash.

##### ✅ **Ejecución**
1. Asegúrate de que `virtualenv` se creó correctamente. Si no, recréalo con:
   ```sh
   python -m venv virtual
   ```
2. Activa el entorno virtual con:
   ```sh
   source virtual/Scripts/activate
   ```
##### 🔍 **Comprobación**
1. Nos deberá aparecer una respuesta parecida a:
    ```sh
    (virtual)
    ```
2. Para comprobar si el entorno esta activado
    ```sh
    which python
    which pip
    ```
3. `which pyhton` nos deberá devolver la ubicación de nuestro entorno de python, ej -> `/c/[...]/virtual/Scripts/python`
4. `which pip` nos deberá devolver la ubicación de nuestro entorno de pip, ej -> `/c/[...]/virtual/Scripts/pip`

##### 🏗️ **Funcionamiento**
Sí se ha activado correctamente en Git Bash, tanto `python` como `pip` apuntan a la ruta dentro de `virtual/`, lo que confirma que estás trabajando dentro del entorno virtual.

Ahora, cualquier paquete que instales con `pip install` se instalará solo dentro de este entorno sin afectar el Python global. 🚀

##### 🗑️ **Desactivación y eliminación**
Cuando quieras **salir del entorno virtual** y volver a usar el Python global, simplemente ejecuta:  

```sh
deactivate
```

Después de hacer eso, si pruebas `which python` o `which pip`, deberían apuntar a la instalación global de Python en tu sistema en lugar del entorno virtual.  



- 🔄 **Alternar entre Python global y el entorno virtual**  

    1️⃣ **Activar el entorno virtual (cuando quieras usarlo)**  
    ```sh
    source virtual/Scripts/activate  # En Git Bash
    ```
    o  
    ```powershell
    virtual\Scripts\activate  # En PowerShell
    ```

    2️⃣ **Salir del entorno virtual (cuando no lo necesites)**  
    ```sh
    deactivate
    ```

    Así puedes elegir si instalar paquetes dentro del entorno virtual o usar el Python global. 🚀

- 🗑️ **Eliminar el entorno virtual definitivamente ⚠️**

    Si decides eliminar el entorno virtual y no lo necesitas más, sigue estos pasos:

    1. **Asegúrate de estar fuera del entorno virtual**:
    Ejecuta `deactivate` si el entorno está activo.

    2. **Elimina la carpeta del entorno virtual**:
    El entorno virtual es simplemente una carpeta en tu proyecto, por lo que puedes eliminarla de manera segura. Utiliza el siguiente comando para eliminarla:

    ```sh
    rm -rf virtual  # En Git Bash o terminal de Linux/macOS
    ```


### PowerShell
#### 🚀 **Ejecución en PowerShell: Habilitar ejecución de scripts**
PowerShell tiene restricciones de seguridad para evitar la ejecución de scripts `.ps1`. Para permitir la activación de entornos virtuales, sigue estos pasos:

##### ✅ **Ejecución**

1. **Abre PowerShell como Administrador** (haz clic derecho en el menú de inicio → *Ejecutar como Administrador*).
2. Ejecuta este comando para permitir la ejecución de scripts en el sistema:
   ```powershell
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
3. Confirma con `Y` y presiona **Enter**.
4. Ahora intenta activar el entorno virtual con:
   ```powershell
   virtual\Scripts\Activate
   ```
   O con el comando más estándar:
   ```powershell
   .\virtual\Scripts\Activate
   ```

Si necesitas más seguridad, puedes volver a restringir la ejecución de scripts con:
```powershell
Set-ExecutionPolicy Restricted -Scope CurrentUser
```




### 🔥 **Resumen rápido**
| Shell | Comando de activación |
|---|---|
| **PowerShell** | `.\virtual\Scripts\Activate` *(requiere cambiar Execution Policy)* |
| **Git Bash** | `source virtual/Scripts/activate` |

