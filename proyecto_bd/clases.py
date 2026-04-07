class Maestro:
    def __init__(
        self,
        matricula_maestro,
        nombre_maestro,
        apellido_paterno,
        apellido_materno,
        correo,
        estatus,
        grado_estudios,
        perfil_docente,
        carga_academica,
        tipo_contrato,
        cedula_profesional,
    ):
        self.matricula_maestro = matricula_maestro
        self.nombre_maestro = nombre_maestro
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.correo = correo
        self.estatus = estatus
        self.grado_estudios = grado_estudios
        self.perfil_docente = perfil_docente
        self.carga_academica = carga_academica
        self.tipo_contrato = tipo_contrato
        self.cedula_profesional = cedula_profesional
        
        # lista de grupos que imparte
        self.grupos = []

class Alumno:
	def __init__(
		self,
		numero_control,
		nombre_alumno,
		apellido_paterno,
		apellido_materno,
		correo_alumno,
		carrera,
		semestre,
		estatus_alumno,
	):
		self.numero_control = numero_control
		self.nombre_alumno = nombre_alumno
		self.apellido_paterno = apellido_paterno
		self.apellido_materno = apellido_materno
		self.correo_alumno = correo_alumno
		self.carrera = carrera
		self.semestre = semestre
		self.estatus_alumno = estatus_alumno

class Grupo:
    def __init__(
        self,
        id_grupo,
        matricula_maestro,
        id_materia,
        salon,
        hora_inicio,
        hora_fin,
        dias,
    ):
        self.id_grupo = id_grupo
        self.matricula_maestro = matricula_maestro
        self.id_materia = id_materia
        self.salon = salon
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.dias = dias

class Materia:
    def __init__(
        self,
        id_materia,
        nombre_materia,
        horas_semana,
        creditos,
        tipo
    ):
        self.id_materia = id_materia
        self.nombre_materia = nombre_materia
        self.horas_semana = horas_semana
        self.creditos = creditos
        self.tipo = tipo
class Horario:
    def __init__(
        self,
        id_horario,
        id_grupo,
        hora_inicio,
        hora_fin,
        dias
    ):
        self.id_horario = id_horario
        self.id_grupo = id_grupo
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.dias = dias

class Actividad:
    def __init__(
        self,
        id_actividad,
        id_unidad,
        id_grupo,
        id_materia,
        nombre_actividad,
        fecha_entrega,
        descripcion,
        valor_porcentaje,
        fecha_asignacion,
        tipo,
        matricula_maestro
        
    ):
        self.id_actividad = id_actividad
        self.id_unidad = id_unidad
        self.id_grupo = id_grupo
        self.id_materia = id_materia
        self.nombre_actividad = nombre_actividad
        self.descripcion = descripcion
        self.fecha_entrega = fecha_entrega
        self.valor_porcentaje = valor_porcentaje
        self.fecha_asignacion = fecha_asignacion
        self.tipo = tipo
        self.matricula_maestro = matricula_maestro

class Unidad:
    def __init__(
        self,
        id_unidad,
        id_materia,
        numero_unidad,
        tema_unidad,
        descripcion
    ):
        self.id_unidad = id_unidad
        self.id_materia = id_materia
        self.numero_unidad = numero_unidad
        self.tema_unidad = tema_unidad
        self.descripcion = descripcion

class Registro:
      def __init__(
        self,
        id_resgitro,
        numero_control,
        id_grupo,
        fecha_registro,
        estatus_materia,
        materia_final,
        tipo_registro
    ):
        self.id_registro = id_resgitro
        self.numero_control = numero_control
        self.id_grupo = id_grupo
        self.fecha_registro = fecha_registro
        self.estatus_materia = estatus_materia
        self.materia_final = materia_final
        self.tipo_registro = tipo_registro

class Resultado:
    def __init__(
        self,
        id_resultado,
        id_registro,
        id_actividad,
        calificacion_unidad,
        fecha_registro,
        observaciones
    ):
        self.id_resultado = id_resultado
        self.id_registro = id_registro
        self.id_actividad = id_actividad
        self.calificacion_unidad = calificacion_unidad
        self.fecha_registro = fecha_registro
        self.observaciones = observaciones
        self.fecha_registro = fecha_registro

class BonusMateria:
    def __init__(
        self,
        id_bonusMateria,
        id_materia,
        id_registro,
        valor,
        justificacion
    ):
        self.id_bonus = id_bonusMateria
        self.id_materia = id_materia
        self.id_registro = id_registro
        self.valor = valor
        self.justificacion = justificacion

class BonusUnidad:
    def __init__(
        self,
        id_bonusUnidad,
        id_registro,
        id_unidad,
        valor,
        justificacion
    ):
        self.id_bonus = id_bonusUnidad
        self.id_registro = id_registro
        self.id_unidad = id_unidad
        self.valor = valor
        self.justificacion = justificacion