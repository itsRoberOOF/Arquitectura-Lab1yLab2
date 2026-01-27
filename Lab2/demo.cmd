-- Crear objetos y provocar violaciones

-- 1) Objetos base
!create t1 : Tutor
!set t1.nombre := 'Carlos Tutor'
!set t1.especialidad := 'Arquitectura'

!create e1 : Estudiante
!set e1.nombre := 'Ana Estudiante'
!set e1.carnet := 'AB2026'

-- 2) Disponibilidades
!create d1 : Disponibilidad
!set d1.fechaHora := '2026-01-20T10:00'
!set d1.estado := #LIBRE
!insert (t1, d1) into TutorDisponibilidad

!create d2 : Disponibilidad
!set d2.fechaHora := '2026-01-20T11:00'
!set d2.estado := #OCUPADA
!insert (t1, d2) into TutorDisponibilidad

-- 3) Reserva valida
!create r1 : Reserva
!set r1.fechaHora := '2026-01-20T10:00'
!set r1.estado := #CONFIRMADA
!insert (t1, r1) into TutorReserva
!insert (e1, r1) into EstudianteReserva

-- 4) Reserva duplicada (misma fechaHora)
!create r2 : Reserva
!set r2.fechaHora := '2026-01-20T10:00'
!set r2.estado := #CREADA
!insert (t1, r2) into TutorReserva
!insert (e1, r2) into EstudianteReserva