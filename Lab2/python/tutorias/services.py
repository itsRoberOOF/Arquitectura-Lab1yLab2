from __future__ import annotations
from dataclasses import replace
from uuid import uuid4
from .domain import EstadoDisponibilidad, EstadoReserva, Estudiante, Reserva, Tutor
from .repositories import InMemoryDisponibilidadRepo, InMemoryReservaRepo


class DomainError(RuntimeError):
    pass


class ReservaService:
    def __init__(
        self, disp_repo: InMemoryDisponibilidadRepo, reserva_repo: InMemoryReservaRepo
    ) -> None:
        self.disp_repo = disp_repo
        self.reserva_repo = reserva_repo

    def crear_reserva(
        self, estudiante: Estudiante, tutor: Tutor, fecha_hora: str
    ) -> Reserva:
        disponibilidad = self.disp_repo.find_free(tutor.id, fecha_hora)
        if not disponibilidad:
            raise DomainError(
                "No hay disponibilidad LIBRE del tutor para esa fecha/hora."
            )
        for r in self.reserva_repo.list_by_tutor(tutor.id):
            if r.fecha_hora == fecha_hora and r.estado not in (
                EstadoReserva.CANCELADA,
                EstadoReserva.EXPIRADA,
            ):
                raise DomainError(
                    "Ya existe una reserva activa del tutor en esa fecha/hora."
                )
        reserva = Reserva(
            id=str(uuid4()),
            tutor_id=tutor.id,
            estudiante_id=estudiante.id,
            fecha_hora=fecha_hora,
            estado=EstadoReserva.CREADA,
        )
        self.reserva_repo.add(reserva)
        self.disp_repo.set_state(disponibilidad.id, EstadoDisponibilidad.OCUPADA)
        return reserva

    def cancelar_reserva(self, reserva_id: str) -> Reserva:
        reserva = self.reserva_repo.get(reserva_id)
        if reserva.estado not in (EstadoReserva.CREADA, EstadoReserva.CONFIRMADA):
            raise DomainError(
                "Solo se puede cancelar una reserva si está CREADA o CONFIRMADA."
            )
        reserva_cancelada = replace(reserva, estado=EstadoReserva.CANCELADA)
        self.reserva_repo.update(reserva_cancelada)
        return reserva_cancelada
