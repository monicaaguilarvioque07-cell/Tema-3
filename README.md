# Generador de Carnés de Empleados

## Descripción

Aplicación en Python que genera carnés corporativos profesionales con foto de perfil circular, información del empleado y branding corporativo.

## Características

- Generación de carnés con foto de perfil en formato circular
-  Personalizable con colores corporativos
-  Información del empleado (nombre, cargo, ID)
-  Manejo de excepciones para archivos faltantes
-  Exportación en formato PNG

## Requisitos

- Python 3.7+
- Pillow (PIL)

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/tuusuario/generador-carnets.git
cd generador-carnets
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

1. Personaliza los datos en `generador_base.py`:
   - `NOMBRE_EMPLEADO`: Nombre del empleado
   - `CARGO_EMPLEADO`: Puesto del empleado
   - `ID_EMPLEADO`: ID corporativo
   - `COLOR_MARCA`: Color corporativo (HEX)

2. Asegúrate de tener en la misma carpeta:
   - `perfil.jpg`: Foto de perfil del empleado
   - `arial.ttf`: Fuente TTF (opcional, usa fuente por defecto si no existe)

3. Ejecuta el script:
```bash
python generador_base.py
```

4. Se generará un archivo PNG con el carné: `carnet_NOMBRE_EMPLEADO.png`

