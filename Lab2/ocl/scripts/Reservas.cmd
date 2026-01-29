-- =========================
-- 1) Crear objetos base
-- =========================
!create t1 : Tutor
!set t1.nombre := 'Carlos Tutor'
!create e1 : Estudiante
!set e1.nombre := 'Ana Estudiante'
-- =========================
-- 2) Crear disponibilidades (para la regla 4)
-- =========================
!create d1 : Disponibilidad
!set d1.fechaHora := '2026-01-20T10:00'
!set d1.estado := #LIBRE
!insert (t1, d1) into TutorDisponibilidad
!create d2 : Disponibilidad
!set d2.fechaHora := '2026-01-20T11:00'
!set d2.estado := #OCUPADA
!insert (t1, d2) into TutorDisponibilidad
-- =========================
-- 3) Crear una reserva válida
-- =========================
!create r1 : Reserva
!set r1.fechaHora := '2026-01-20T10:00'
!set r1.estado := #CONFIRMADA
!insert (t1, r1) into TutorReserva
!insert (e1, r1) into EstudianteReserva
-- =========================
-- 4) Crear una reserva duplicada (misma fechaHora) para violar la regla 3
-- =========================
!create r2 : Reserva
!set r2.fechaHora := '2026-01-20T10:00'
!set r2.estado := #CREADA
!insert (t1, r2) into TutorReserva
!insert (e1, r2) into EstudianteReserva
-- =========================
-- 5) Crear una reserva con estado "sin asignar" para provocar problemas
-- (En algunos entornos queda undefined y puede romper EstadoValido)
-- =========================
!create r3 : Reserva
!set r3.fechaHora := '2026-01-20T12:00'
!insert (t1, r3) into TutorReserva
!insert (e1, r3) into EstudianteReserva
