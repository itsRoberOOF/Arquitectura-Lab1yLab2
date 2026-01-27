# Laboratorios 1 y 2 - Sistema de reserva de tutorías

Este repositorio contiene el desarrollo de dos laboratorios centrados en un sistema de reservas de tutorías, combinando modelado UML, validación con USE + OCL y una implementación funcional en Python + FastAPI bajo una arquitectura en capas.

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
└─ diagramas/
   ├─ DiagramaCajasPrincipales.png
   └─ DiagramaContexto.png
```
### Contenido de las carpetas

- **app/**: contiene la implementación del sistema organizada en **capas**:
  - **domain/**: modelos y errores del negocio, junto con las reglas asociadas.
  - **application/**: servicio principal que implementa el caso de uso para **crear reservas**.
  - **infrastructure/**: repositorio en memoria para almacenar datos.
  - **api/**: endpoint en **FastAPI** que recibe solicitudes, llama al caso de uso y traduce errores de negocio a respuestas HTTP.

- **tests/**: contiene **pruebas básicas con pytest**, enfocadas en validar las reglas de negocio.

- **diagramas/**: contiene los diagramas del laboratorio, incluyendo el **diagrama de contexto** y el **diagrama de cajas principales**.
