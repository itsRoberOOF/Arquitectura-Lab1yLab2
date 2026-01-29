from __future__ import annotations
from dataclasses import dataclass
from enum import Enum


class EstadoReserva(str, Enum):
    CREADA = "CREADA"
    CONFIRMADA = "CONFIRMADA"
    CANCELADA = "CANCELADA"
    EXPIRADA = "EXPIRADA"


class EstadoDisponibilidad(str, Enum):
    LIBRE = "LIBRE"
    OCUPADA = "OCUPADA"


@dataclass
class Tutor:
    id: str
    nombre: str
    especialidad: str


@dataclass
class Estudiante:
    id: str
    nombre: str
    carnet: str


@dataclass
class Disponibilidad:
    id: str
    tutor_id: str
    fecha_hora: str
    estado: EstadoDisponibilidad


@dataclass
class Reserva:
    id: str
    tutor_id: str
    estudiante_id: str
    fecha_hora: str
    estado: EstadoReserva
