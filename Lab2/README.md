# Laboratorios 1 y 2 - Sistema de reserva de tutorías

Este repositorio contiene el desarrollo de dos laboratorios centrados en un sistema de reservas de tutorías, combinando modelado UML, validación con USE + OCL y una implementación funcional en Python + FastAPI bajo una arquitectura en capas.{

- Estudiante: Roberto Morán

## 🛠️ Requisitos

- **Python** para ejecutar los test de python
- **Java 8+** para ejecutar USE
- **USE** para ejecutar modelos y validaciones

## Laboratorio 2

El Laboratorio 2 se enfoca en el **Sistema de Reservas de Tutorías**, combinando
**modelado UML**, **validación formal con USE + OCL** y una
**implementación funcional en Python**, siguiendo el flujo UML → OCL →
Código

### 📁 Estructura

    Lab2/
    ├── diagramas/
    │   ├── DiagramaCasoDeUso.pdf
    │   ├── DiagramaClases.pdf
    │   ├── DiagramaEstados.pdf
    │   └── DiagramaSecuencia.pdf
    │
    ├── evidencias/
    │   ├── Cars-Open-Check-Consultas.png
    │   ├── Reservas-Correccion.png
    │   ├── Reservas-Open-Check.png
    │   ├── TestsPython.png
    │   ├── Tutorias-Correccion.png
    │   ├── Tutorias-Open-Check.png
    │   ├── University-Correccion.png
    │   └── University-Open-Check.png
    │
    ├── ocl/
    │   └── scripts/
    |   │      ├── Cars.cmd
    |   │      ├── Reservas.cmd
    |   │      ├── Tutorias.cmd
    |   │      ├── University.cmd
    |   ├── Cars.use
    |   ├── Reservas.use
    |   ├── Tutorias.use
    |   └── University.use
    │
    ├── python/
    │   ├── tutorias/
    │   │   ├── __init__.py
    │   │   ├── domain.py
    │   │   ├── repositories.py
    │   │   └── services.py
    │   │
    │   └── tests/
    │       └── test_reservas.py
    │
    └── TablaTrazabilidad.pdf

### 📝 Contenido de las carpetas

**diagramas/**

Contiene los **diagramas UML exportados en PDF**: - Diagrama de Casos de
Uso\

- Diagrama de Clases\
- Diagrama de Secuencia "Crear Reserva"\
- Diagrama de Estados de la Reserva

---

**evidencias/**

Capturas de **ejecución en USE** y **pruebas Python**, incluyendo: -
Apertura de modelos (`open`) - Validaciones (`check`) - Correcciones de
violaciones - Evidencia de pruebas automatizadas

---

**ocl/**

Archivos `.use` con los **modelos UML textuales y restricciones OCL**:

- **Cars.use** → ejercicio introductorio de invariantes\
- **University.use** → association class + unicidad\
- **Reservas.use** → modelo simplificado del sistema\
- **Tutorias.use** → modelo completo con invariantes, precondiciones y
  postcondiciones

---

**ocl/scripts**

Archivos `.cmd` con los que **probar los modelos OCL**:

- **Cars.cmd** → modelo de Cars.use
- **University.cmd** → modelo de University.use
- **Reservas.cmd** → modelo de Reservas.use
- **Tutorias.cmd** → modelo de Tutorias.use

---

**python/tutorias/**

Implementación del dominio siguiendo la guía:

- **domain.py** → entidades del dominio (Enums + dataclasses)\
- **repositories.py** → repositorios in-memory\
- **services.py** → lógica de negocio con validaciones OCL traducidas
  a Python

---

**python/tests/**

Archivo de pruebas automatizadas:

- **test_reservas.py** → valida reglas de negocio como:
    - Crear reserva válida\
    - Falla sin disponibilidad\
    - Falla por doble reserva\
    - Cancelación válida\
    - Cancelación inválida

---

**TablaTrazabilidad.pdf**

Tabla que documenta la relación entre: - Elementos UML\

- Restricciones OCL\
- Implementación Python\
- Pruebas automatizadas

### ▶️ Instrucciones de ejecución (USE + OCL + Python)

Esta sección describe cómo ejecutar **cada modelo OCL**, sus **scripts
`.cmd`** y las **pruebas en Python**, siguiendo el flujo del
laboratorio.

---

## 🧪 Ejecución en USE (OCL)

Antes de iniciar, abre USE desde la carpeta donde lo tengas instalado.

---

### ▶️ 1. Ejecutar Cars.use (Ejercicio introductorio)

**Cargar el modelo (o cargarlo desde la aplicación):**

    use Cars.use

**Ejecutar el script:**

    open scripts/Cars.cmd

**Validar invariantes:**

    check

**Consultas opcionales:**

    ? Car.allInstances()->size()
    ? Car.allInstances()->select(c | c.mileage < 0)
    ? Car.allInstances()->forAll(c | c.mileage >= 0)

---

### ▶️ 2. Ejecutar University.use (Association Class)

**Cargar el modelo (o cargarlo desde la aplicación):**

    use University.use

**Ejecutar el script:**

    open scripts/University.cmd

**Validar invariantes:**

    check

**Corregir violación (si aplica):**

    !set s2.email := 'luis@uni.edu'
    check

---

### ▶️ 3. Ejecutar Reservas.use (Modelo simplificado)

**Cargar el modelo (o cargarlo desde la aplicación):**

    use Reservas.use

**Ejecutar el script:**

    open scripts/Reservas.cmd

**Validar invariantes:**

    check

**Corrección manual:**

    !set r2.estado := #CANCELADA
    !set r3.estado := #CREADA
    check

**Consultas opcionales:**

    ? t1.reservas->size()
    ? t1.reservas->select(r | r.estado = EstadoReserva::CONFIRMADA)
    ? t1.disponibilidades->select(d | d.estado = EstadoDisponibilidad::LIBRE)

---

### ▶️ 4. Ejecutar Tutorias.use (Modelo completo)

**Cargar el modelo (o cargarlo desde la aplicación):**

    use Tutorias.use

**Ejecutar el script:**

    open scripts/Tutorias.cmd

**Validar modelo:**

    check

**Corrección manual**
!set r2.estado := #CANCELADA
check

---

## 🐍 Ejecución del proyecto Python

Entrar a la carpeta `python/`:

    cd python

---

### ▶️ Ejecutar pruebas con pytest (recomendado)

Instalar pytest si no está instalado:

    pip install pytest

Ejecutar pruebas:

    python -m pytest tests/test_reservas.py -v

---

### 🎯 Resultado esperado

- Validaciones OCL detectadas y corregidas
- Reglas de negocio implementadas en Python
- **5 pruebas automatizadas pasando correctamente**\
  ℹ️ **Nota:** En la carpeta de evidencias se encuentran capturas de pantalla que muestra el resultado de cada operación/comando de USE y de las pruebas unitarias de Python.

---

### 📌 Flujo del laboratorio

**Requisitos → UML → OCL → USE → Python → Tests → Trazabilidad**
