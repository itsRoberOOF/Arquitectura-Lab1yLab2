from fastapi import FastAPI, HTTPException
from datetime import datetime
from app.application.services import ReservaService
from app.infrastructure.repositories import ReservaRepoMemoria
from app.domain.errors import ReglaNegocioError

app = FastAPI(title="Tutorías API")

repo = ReservaRepoMemoria()
service = ReservaService(repo)


# Endpoint
@app.post("/reservas")
def crear_reserva(estudiante_id: str, tutor_id: str, fecha_hora: str):
    try:
        # Formateo de hora y fecha
        dt = datetime.fromisoformat(fecha_hora)
        # Llamada al servicio para crear la reserva
        r = service.crear_reserva(estudiante_id, tutor_id, dt)
        return {"id": r.id, "estado": r.estado}
    except ReglaNegocioError as e:
        # Si hay algun error, retorna una respuesta HTTP con el error 400
        raise HTTPException(status_code=400, detail=str(e))
