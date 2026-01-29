import unittest

from tutorias.domain import (
    Disponibilidad,
    EstadoDisponibilidad,
    EstadoReserva,
    Estudiante,
    Tutor,
)
from tutorias.repositories import InMemoryDisponibilidadRepo, InMemoryReservaRepo
from tutorias.services import DomainError, ReservaService


class TestReservaService(unittest.TestCase):
    def setUp(self) -> None:
        self.tutor = Tutor(id="t1", nombre="Carlos Tutor", especialidad="Arquitectura")
        self.estudiante = Estudiante(id="e1", nombre="Ana Estudiante", carnet="AB2026")
        self.disp_repo = InMemoryDisponibilidadRepo()
        self.res_repo = InMemoryReservaRepo()
        self.service = ReservaService(self.disp_repo, self.res_repo)
        self.disp_repo.add(
            Disponibilidad(
                id="d1",
                tutor_id=self.tutor.id,
                fecha_hora="2026-01-20T10:00",
                estado=EstadoDisponibilidad.LIBRE,
            )
        )

    def test_crear_reserva_ok(self):
        r = self.service.crear_reserva(self.estudiante, self.tutor, "2026-01-20T10:00")
        self.assertEqual(r.estado, EstadoReserva.CREADA)
        self.assertEqual(r.fecha_hora, "2026-01-20T10:00")

    def test_crear_reserva_falla_sin_disponibilidad(self):
        with self.assertRaises(DomainError):
            self.service.crear_reserva(self.estudiante, self.tutor, "2026-01-20T11:00")

    def test_crear_reserva_falla_doble_reserva_activa(self):
        self.service.crear_reserva(self.estudiante, self.tutor, "2026-01-20T10:00")
        with self.assertRaises(DomainError):
            self.service.crear_reserva(self.estudiante, self.tutor, "2026-01-20T10:00")

    def test_cancelar_reserva_ok(self):
        r = self.service.crear_reserva(self.estudiante, self.tutor, "2026-01-20T10:00")
        r2 = self.service.cancelar_reserva(r.id)
        self.assertEqual(r2.estado, EstadoReserva.CANCELADA)

    def test_cancelar_reserva_falla_si_no_activa(self):
        r = self.service.crear_reserva(self.estudiante, self.tutor, "2026-01-20T10:00")
        r2 = self.service.cancelar_reserva(r.id)
        with self.assertRaises(DomainError):
            self.service.cancelar_reserva(r2.id)


if __name__ == "__main__":
    unittest.main()
