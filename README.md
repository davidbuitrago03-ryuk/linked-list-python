# Linked List en Python

Implementación de una lista enlazada simple en Python, con operaciones de inserción, búsqueda, eliminación e inversión (iterativa y recursiva).

---

## Requisitos

- Python 3.8 o superior
- PyCharm Community Edition (recomendado) o cualquier editor de texto

---

## 1. Instalar Python en Windows

1. Ve a https://www.python.org/downloads/
2. Descarga el instalador de la versión más reciente (Python 3.x).
3. Ejecuta el instalador. **Importante:** marca la casilla _"Add Python to PATH"_ antes de instalar.
4. Para verificar la instalación, abre el símbolo del sistema (`cmd`) y ejecuta:

```
python --version
```

Deberías ver algo como `Python 3.12.0`.

---

## 2. Instalar PyCharm en Windows

1. Ve a https://www.jetbrains.com/pycharm/download/
2. Descarga la versión **Community** (gratuita).
3. Ejecuta el instalador y sigue los pasos. Las opciones por defecto son suficientes.

---

## 3. Crear el proyecto en PyCharm

1. Abre PyCharm y haz clic en **New Project**.
2. En _Location_, elige la carpeta donde quieres guardar el proyecto.
3. En _Interpreter type_, selecciona **Project venv** — esto crea un entorno virtual aislado solo para este proyecto. Es la opción por defecto en versiones recientes de PyCharm.
4. Haz clic en **Create**.
5. Haz clic derecho sobre la carpeta raíz del proyecto → **New** → **Python File** → escribe `linked_list` → Enter.
6. Copia el contenido del archivo `linked_list.py` de este repositorio y pégalo en el archivo recién creado.

---

## 4. Correr el programa

### Desde PyCharm

Con el archivo `linked_list.py` abierto, haz clic derecho en el editor y selecciona **Run 'linked_list'**, o presiona el botón verde de play en la parte superior derecha.

### Desde la terminal

Abre el símbolo del sistema (`cmd`), navega hasta la carpeta del proyecto y ejecuta:

```
python linked_list.py
```

Salida esperada:

```
Lista inicial:       [0, 1, 2, 3]
Longitud:            4
Contiene el 2:       True
Buscar el 3:         3
Tras eliminar el 2:  [0, 1, 3]
Invertida:           [3, 1, 0]
Invertida de nuevo:  [0, 1, 3]
Recorrido con for:   0 1 3
```
