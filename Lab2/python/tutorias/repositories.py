from __future__ import annotations
from dataclasses import replace
from typing import Dict, List, Optional
from .domain import Disponibilidad, EstadoDisponibilidad, Reserva


class InMemoryDisponibilidadRepo:
    def __init__(self) -> None:
        self._items: Dict[str, Disponibilidad] = {}

    def add(self, d: Disponibilidad) -> None:
        self._items[d.id] = d

    def find_free(self, tutor_id: str, fecha_hora: str) -> Optional[Disponibilidad]:
        for d in self._items.values():
            if (
                d.tutor_id == tutor_id
                and d.fecha_hora == fecha_hora
                and d.estado == EstadoDisponibilidad.LIBRE
            ):
                return d
        return None

    def set_state(self, disponibilidad_id: str, estado: EstadoDisponibilidad) -> None:
        d = self._items[disponibilidad_id]
        self._items[disponibilidad_id] = replace(d, estado=estado)


class InMemoryReservaRepo:
    def __init__(self) -> None:
        self._items: Dict[str, Reserva] = {}

    def add(self, r: Reserva) -> None:
        self._items[r.id] = r

    def get(self, reserva_id: str) -> Reserva:
        return self._items[reserva_id]

    def update(self, r: Reserva) -> None:
        self._items[r.id] = r

    def list_by_tutor(self, tutor_id: str) -> List[Reserva]:
        return [r for r in self._items.values() if r.tutor_id == tutor_id]
