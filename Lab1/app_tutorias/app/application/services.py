from datetime import datetime
from app.domain.errors import ReglaNegocioError


class ReservaService:
    # Constructor
    def __init__(self, reserva_repo):
        self.reserva_repo = reserva_repo

    # Función para crear una reserva
    # @param estudiante_id: ID del estudiante que hace la reserva
    # @param tutor_id: ID del tutor con el que se hace la reserva
    # @param fecha_hora: Fecha y hora de la reserva (datetime)
    def crear_reserva(self, estudiante_id, tutor_id, fecha_hora: datetime):
        # Validaciones
        if fecha_hora < datetime.now():
            raise ReglaNegocioError("No se puede reservar en el pasado.")

        if self.reserva_repo.existe_reserva(tutor_id=tutor_id, fecha_hora=fecha_hora):
            raise ReglaNegocioError("El tutor ya tiene una reserva en ese horario.")

        # Si todo esta bien, se crea utilizando la lógica hecha en el repositorio
        return self.reserva_repo.crear(estudiante_id, tutor_id, fecha_hora)
