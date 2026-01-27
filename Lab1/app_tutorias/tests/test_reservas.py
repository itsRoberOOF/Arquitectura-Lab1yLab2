from datetime import datetime, timedelta
import pytest
from app.application.services import ReservaService
from app.infrastructure.repositories import ReservaRepoMemoria
from app.domain.errors import ReglaNegocioError


# Prueba para validar que una reserva no se pueda crear en el pasado
def test_no_reservar_en_pasado():
    s = ReservaService(ReservaRepoMemoria())
    with pytest.raises(ReglaNegocioError):
        s.crear_reserva("e1", "t1", datetime.now() - timedelta(days=1))


# Prueba para validar que no se pueda crear una doble reserva para el mismo tutor en la misma hora
def test_no_doble_reserva_mismo_tutor_misma_hora():
    repo = ReservaRepoMemoria()
    s = ReservaService(repo)
    dt = datetime.now() + timedelta(days=1)
    s.crear_reserva("e1", "t1", dt)
    with pytest.raises(ReglaNegocioError):
        s.crear_reserva("e2", "t1", dt)
