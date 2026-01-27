import uuid
from app.domain.models import Reserva


# Clase que sirve como memoria para las reservas, simula una db usando una lista en memoria
class ReservaRepoMemoria:
    # Constructor
    def __init__(self):
        self._items = []

    # Función para verificar si existe una reserva para un tutor en una fecha y hora específicas (no debe estar cancelada)
    def existe_reserva(self, tutor_id, fecha_hora):
        return any(
            r.tutor_id == tutor_id
            and r.fecha_hora == fecha_hora
            and r.estado != "CANCELADA"
            for r in self._items
        )

    # Función para crear la reserva en el arreglo de reservas
    def crear(self, estudiante_id, tutor_id, fecha_hora):
        # Usa la estructura definida en el modelo
        r = Reserva(
            id=str(uuid.uuid4()),
            estudiante_id=estudiante_id,
            tutor_id=tutor_id,
            fecha_hora=fecha_hora,
            estado="CREADA",
        )
        self._items.append(r)
        return r
