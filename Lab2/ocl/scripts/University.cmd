-- 1) crear estudiantes
!create s1 : Student
!set s1.id := 1
!set s1.name := 'Ana'
!set s1.email := 'ana@uni.edu'

!create s2 : Student
!set s2.id := 2
!set s2.name := 'Luis'
!set s2.email := 'ana@uni.edu'  -- viola UniqueEmail

-- 2) crear curso
!create c1 : Course
!set c1.code := 'ARQ101'
!set c1.title := 'Arquitectura'
!set c1.credits := 4

-- 3) crear matrícula (Enrollment es association class)
!create e1 : Enrollment
!set e1.grade := 95
!insert (s1, c1) into Enrollment  -- crea el vínculo de la association class