# Laboratorios 1 y 2 - Sistema de reserva de tutorías

Este repositorio contiene el desarrollo de dos laboratorios centrados en un sistema de reservas de tutorías, combinando modelado UML, validación con USE + OCL y una implementación funcional en Python + FastAPI bajo una arquitectura en capas.{

- Estudiante: Roberto Morán

## 🛠️ Requisitos

- **Python** para ejecutar la aplicación del Laboratorio 1.
- **USE** para ejecutar el modelo y las validaciones del Laboratorio 2.


## Laboratorio 1
El Laboratorio 1 desarrolla una aplicación en **Python + FastAPI** con **arquitectura en capas**, enfocada en la separación de responsabilidades y la validación de reglas mediante **pruebas automatizadas**.

### 📁 Estructura
```
Lab1/
├─ app_tutorias/
│  ├─ app/
│  │  ├─ api/
│  │  │  ├─ __init__.py
│  │  │  └─ main.py
│  │  ├─ application/
│  │  │  ├─ __init__.py
│  │  │  └─ services.py
│  │  ├─ domain/
│  │  │  ├─ __init__.py
│  │  │  ├─ errors.py
│  │  │  └─ models.py
│  │  └─ infrastructure/
│  │     ├─ __init__.py
│  │     └─ repositories.py
│  ├─ tests/
│  │  └─ test_reservas.py
│  └─ requirements.txt
│
└─ media/
   ├─ DiagramaCajasPrincipales.png
   └─ DiagramaContexto.png
   └─ ResultadoPruebas.png
   └─ ResultadoServer.png
   └─ ResultadoRequest.png
```
### 📝 Contenido de las carpetas

- **app/**: contiene la implementación del sistema organizada en **capas**:
  - **domain/**: modelos y errores del negocio, junto con las reglas asociadas.
  - **application/**: servicio principal que implementa el caso de uso para **crear reservas**.
  - **infrastructure/**: repositorio en memoria para almacenar datos.
  - **api/**: endpoint en **FastAPI** que recibe solicitudes, llama al caso de uso y traduce errores de negocio a respuestas HTTP.

- **tests/**: contiene **pruebas básicas con pytest**, enfocadas en validar las reglas de negocio.

- **media/**: contiene los diagramas del laboratorio, incluyendo el **diagrama de contexto** y el **diagrama de cajas principales**, además de capturas con el **resultado esperado** de ciertas operaciones.

### ▶️ Instrucciones de ejecución

Desde la carpeta `Lab1/app_tutorias/`, instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar las pruebas (opción recomendada):

```bash
PYTHONPATH=. pytest -q
```

Levantar el servidor FastAPI:

```bash
PYTHONPATH=. uvicorn app.api.main:app --reload
```

Probar el endpoint de creación de reservas:

```bash
curl -X POST "http://127.0.0.1:8000/reservas?estudiante_id=e1&tutor_id=t1&fecha_hora=2026-01-25T10:30:00"
```

### 🎯 Resultado esperado
- Ejecución correcta de las **pruebas automatizadas** (`pytest`) sin errores.
<img width="620" height="118" alt="ResultadoPruebas" src="https://github.com/user-attachments/assets/a733afb6-ec09-4bd0-b43e-f377de47f291" />

- Servidor levantado **correctamente** con uvicorn.
<img width="1120" height="201" alt="ResultadoServer" src="https://github.com/user-attachments/assets/5a2e1d05-39f1-4ff1-a6ee-d5c86d4a0f26" />

- Validación de la regla que **impide crear reservas en fechas pasadas** al hacer un request. 
<img width="633" height="48" alt="ResultadoRequest" src="https://github.com/user-attachments/assets/2fd62563-290b-4530-ab7a-fcaf417ccd41" />


## Laboratorio 2
El Laboratorio 2 se enfoca en la **validación formal del modelo** mediante **USE + OCL**, además del desarrollo de diagramas UML como parte de los entregables del laboratorio.

### 📁 Estructura
```
Lab2/
├─ tutorias.use
├─ constraints.ocl
├─ demo.cmd
│
└─ media/
   ├─ DiagramaCasosDeUso.png
   ├─ DiagramaClases.png
   ├─ DiagramaEstadosReserva.png
   ├─ DiagramaSecuencia.png
   └─ ResultadoOpen.png
   └─ ResultadoCheck.png
```

### 📝 Contenido de las carpetas

- **tutorias.use**: contiene la definición del **modelo** del sistema en USE.
- **constraints.ocl**: contiene las **restricciones OCL** utilizadas para validar invariantes, precondiciones y postcondiciones.
- **demo.cmd**: script para generar el **estado de ejecución** del modelo.
- **media/**: contiene los **diagramas UML del laboratorio** y una captura con el **resultado esperado**.

### ▶️ Instrucciones de ejecución

> Para que el modelo funcione correctamente, el contenido de `constraints.ocl` debe copiarse al final del archivo `tutorias.use`, dentro de la sección `constraints`.

Pasos:

1. Abrir la aplicación **USE**
2. Cargar el archivo:
```
tutorias.use
```
3. Ejecutar el script:
```
open demo.cmd
```
4. Ejecutar las validaciones:
```
check
```
ℹ️ Las constraints se cargan automaticamente

### 🎯 Resultado esperado
- Al ejecutar el script (demo.cmd) se debe cargar el estado inicial del modelo, lo que mostrara el siguiente mensaje:
<img width="1918" height="903" alt="ResultadoOpen" src="https://github.com/user-attachments/assets/12cb660b-e307-408d-aeef-78fc9f147584" />

- Posteriormente, al ejecutar el check, las restricciones definidas en **OCL** deben validarse correctamente, lo que lanzará el siguiente error (debido a que no pueden existir 2 reservas al mismo tiempo):
<img width="982" height="265" alt="ResultadoCheck" src="https://github.com/user-attachments/assets/e8006a22-1275-4bd8-821c-2d5a593743bf" />

