from django.db import models

# Create your models here.
ESTADOS = [
    #Para el cliente
    ("borrador", "Borrador"), #El cliente todavía no termina de redactar el incidente
    ("activo", "Activo"), #El cliente acaba de subir el incidente y aún no tiene respuesta
    ("dudas", "Pendiente contestar"), #Falta que el cliente conteste dudas
    ("cancelado", "Cancelado"), #Se cancelo el incidente.
    ("finalizado", "Finalizado"), #Se entregó una solución al cliente
    #Estatus internos (el cliente no debe verlos)
    ("suspendido", "Suspendido"), #Se suspendió la atención del incidente para atender otros temas
    ("enCurso", "En curso"), #Se esta atendiendo el incidente
    ("faltaEntrega", "Falta entregar"), #Se terminó de atender, pero falta generar la entrega
    
]
class Usuarios(models.Model):
    id_Usr     = models.AutoField(verbose_name="id", primary_key=True, null=False)
    correo     = models.CharField(verbose_name="Correo", max_length=80, blank=True, null=False, default="")
    password   = models.CharField(verbose_name="Contraseña", max_length=256, blank=True, null=False, default="")
    ult_login  = models.DateTimeField(verbose_name="Último login", editable=False)
    token      = models.CharField(verbose_name="Último token", max_length=256, blank=True, null=False, default="")
    fh_alta    = models.DateTimeField(verbose_name="Fecha alta", editable=False, auto_now_add=True)
    fh_mod     = models.DateTimeField(verbose_name="Fecha modificación", editable=False, auto_now=True)

class Categorias(models.Model):    
    id_categoria = models.AutoField(verbose_name="id", primary_key=True, null=False)
    nombre       = models.CharField(verbose_name="Nombre", max_length=128, blank=True, null=False, default="")
    fh_alta      = models.DateTimeField(verbose_name="Fecha alta", editable=False, auto_now_add=True)
    fh_mod       = models.DateTimeField(verbose_name="Fecha modificación", editable=False, auto_now=True)

class Pais(models.Model):
    id_pais  = models.AutoField(verbose_name="id", primary_key=True, null=False)
    nombre   = models.CharField(verbose_name="Nombre", max_length=128, blank=True, null=False, default="")
    fh_alta  = models.DateTimeField(verbose_name="Fecha alta", editable=False, auto_now_add=True)
    fh_mod   = models.DateTimeField(verbose_name="Fecha modificación", editable=False, auto_now=True)

class Estado(models.Model):
    id_estado = models.AutoField(verbose_name="id", primary_key=True, null=False)
    id_pais   = models.IntegerField(verbose_name="id País") #Pais.id
    nombre    = models.CharField(verbose_name="Nombre", max_length=128, blank=True, null=False, default="")
    fh_alta   = models.DateTimeField(verbose_name="Fecha alta", editable=False, auto_now_add=True)
    fh_mod    = models.DateTimeField(verbose_name="Fecha modificación", editable=False, auto_now=True)

class Ciudad(models.Model):
    id_ciudad = models.AutoField(verbose_name="id", primary_key=True, null=False)
    id_estado = models.IntegerField(verbose_name="id estado") #Estado.id
    id_pais   = models.IntegerField(verbose_name="id país") #Pais.id
    nombre    = models.CharField(verbose_name="Nombre", max_length=128, blank=True, null=False, default="")
    fh_alta   = models.DateTimeField(verbose_name="Fecha alta", editable=False, auto_now_add=True)
    fh_mod    = models.DateTimeField(verbose_name="Fecha modificación", editable=False, auto_now=True)
"""
    #JABM(02/02/2025): Creo que no es necesario el uso de este catálogo.
class Codigo_Postal(models.Model):
    id_Cp     = models.AutoField(verbose_name="id", primary_key=True, null=False)
    id_ciudad = models.IntegerField(verbose_name="id ciudad") #Ciudad.id
    id_estado = models.IntegerField(verbose_name="id estado") #Estado.id
    id_pais   = models.IntegerField(verbose_name="id país") #Pais.id
    alias     = models.CharField(verbose_name="Alias", max_length=16, blank=True, null=False, default="")
    nombre    = models.CharField(verbose_name="Nombre", max_length=128, blank=True, null=False, default="")
    fh_alta   = models.DateTimeField(verbose_name="Fecha alta", editable=False, auto_now_add=True)
    fh_mod    = models.DateTimeField(verbose_name="Fecha modificación", editable=False, auto_now=True)
"""
class Personas(models.Model):
    id_pers      = models.AutoField(verbose_name="id", primary_key=True, null=False)
    id_categoria = models.IntegerField(verbose_name="Id categoria") #Categorias.id
    activo       = models.BooleanField(verbose_name="Activo", default=False)
    alias        = models.CharField(verbose_name="Alias", max_length=16, blank=True, null=False, default="")
    nombre       = models.CharField(verbose_name="Nombre", max_length=128, blank=True, null=False, default="")
    id_pais      = models.IntegerField(verbose_name="id País") #Pais.id
    id_estado    = models.IntegerField(verbose_name="id Estado") #Estado.id
    id_ciudad    = models.IntegerField(verbose_name="id ciudad") #Ciudad.id
    #JABM(02/02/2025) No creo conveniente utilizar el catálogo de cód. postal
    #id_Cp       = models.IntegerField(verbose_name="id cód. Postal") #Codigo_Postal.id
    cod_postal   = models.CharField(verbose_name="Código postal", max_length=16, blank=True, null=False, default="")
    direccion    = models.CharField(verbose_name="Dirección", max_length=128, blank=True, null=False, default="")
    referencia   = models.CharField(verbose_name="Referencia", max_length=128, blank=True, null=False, default="")
    telefono     = models.CharField(verbose_name="Teléfono", max_length=32, blank=True, null=False, default="")
    celular      = models.CharField(verbose_name="Celular", max_length=32, blank=True, null=False, default="")
    fh_alta      = models.DateTimeField(verbose_name="Fecha alta", editable=False, auto_now_add=True)
    fh_mod       = models.DateTimeField(verbose_name="Fecha modificación", editable=False, auto_now=True)

class Inc_Clasificacion(models.Model):
    id_inc_clas = models.AutoField(verbose_name="id", primary_key=True, null=False)
    nombre      = models.CharField(verbose_name="Nombre", max_length=128, blank=True, null=False, default="")
    fh_alta     = models.DateTimeField(verbose_name="Fecha alta", editable=False, auto_now_add=True)
    fh_mod      = models.DateTimeField(verbose_name="Fecha modificación", editable=False, auto_now=True)

class Inc_Gravedad(models.Model):
    id_inc_gravedad = models.AutoField(verbose_name="id", primary_key=True, null=False)
    nombre          = models.CharField(verbose_name="Nombre", max_length=128, blank=True, null=False, default="")
    fh_alta         = models.DateTimeField(verbose_name="Fecha alta", editable=False, auto_now_add=True)
    fh_mod          = models.DateTimeField(verbose_name="Fecha modificación", editable=False, auto_now=True)

class Archivos_Locales(models.Model):
    id_file_loc   = models.AutoField(verbose_name="id", primary_key=True, null=False)
    activo        = models.BooleanField(verbose_name="Activo", default=False)
    nombre        = models.CharField(verbose_name="Nombre", max_length=128, blank=True, null=False, default="")
    data_file_b64 = models.TextField(verbose_name="Contenido del archivo b64")
    id_pers       = models.IntegerField(verbose_name="Id personal") #Personas.id_pers
    fh_alta       = models.DateTimeField(verbose_name="Fecha alta", editable=False, auto_now_add=True)
    fh_mod        = models.DateTimeField(verbose_name="Fecha modificación", editable=False, auto_now=True)    

class Archivos_Ftp(models.Model):
    id_Ftp   = models.AutoField(verbose_name="id", primary_key=True, null=False)
    activo   = models.BooleanField(verbose_name="Activo", default=False)
    nombre   = models.CharField(verbose_name="Nombre", max_length=128, blank=True, null=False, default="")
    ruta     = models.CharField(verbose_name="Ruta del archivo", max_length=256, blank=True, null=False, default="") 
    id_pers       = models.IntegerField(verbose_name="Id personal") #Personas.id_pers
    fh_alta  = models.DateTimeField(verbose_name="Fecha alta", editable=False, auto_now_add=True)
    fh_mod   = models.DateTimeField(verbose_name="Fecha modificación", editable=False, auto_now=True)

class IncidentesC(models.Model):
    id_Incidente_c  = models.AutoField(verbose_name="id", primary_key=True, null=False)
    id_inc_clas     = models.IntegerField(verbose_name="Id clasificación") #Inc_Clasificacion.id_inc_clas
    id_inc_gravedad = models.IntegerField(verbose_name="Id gravedad") #Inc_Gravedad.id_inc_gravedad
    id_pers         = models.IntegerField(verbose_name="Id personal") #Personas.id_pers
    nombre          = models.CharField(verbose_name="Titulo del incidente", max_length=128, blank=True, null=False, default="")
    detalle         = models.TextField(verbose_name="Contenido")
    estatus         = models.CharField(max_length=16, choices=ESTADOS, default="borrador")
    activo          = models.BooleanField(verbose_name="Activo", default=False)
    fh_estimada     = models.DateTimeField(verbose_name="Fecha estimada")
    fh_compromiso   = models.DateTimeField(verbose_name="Fecha compromiso")
    fh_alta         = models.DateTimeField(verbose_name="Fecha alta", editable=False, auto_now_add=True)
    fh_mod          = models.DateTimeField(verbose_name="Fecha modificación", editable=False, auto_now=True)

class IncidentesD(models.Model):
    id_incidente_c  = models.IntegerField(verbose_name="Id incidente", primary_key=True, null=False)
    id_incidente_d  = models.IntegerField(verbose_name="Id Respuesta", primary_key=True, null=False)
    id_Pers         = models.IntegerField(verbose_name="Id personal") #Personas.id_pers
    nombre          = models.CharField(verbose_name="Titulo de la respuesta", max_length=128, blank=True, null=False, default="")
    detalle         = models.TextField(verbose_name="Contenido")
    activo          = models.BooleanField(verbose_name="Activo", default=False)
    fh_alta         = models.DateTimeField(verbose_name="Fecha alta", editable=False, auto_now_add=True)
    fh_mod          = models.DateTimeField(verbose_name="Fecha modificación", editable=False, auto_now=True)

class Adjuntos(models.Model):
    id_incidente_c = models.IntegerField(verbose_name="Id incidente", primary_key=True, null=False)
    id_incidente_d = models.IntegerField(verbose_name="Id Respuesta", primary_key=True, null=False)
    id_adjunto     = models.IntegerField(verbose_name="Id adjunto", primary_key=True, null=False)
    activo         = models.BooleanField(verbose_name="Activo", default=False)
    id_ftp         = models.AutoField(verbose_name="id del FTP") #Archivos_Ftp.id_ftp
    id_file_loc    = models.AutoField(verbose_name="id del archivo local") #Archivos_Locales.id_file_loc
    fh_alta        = models.DateTimeField(verbose_name="Fecha alta", editable=False, auto_now_add=True)
    fh_mod         = models.DateTimeField(verbose_name="Fecha modificación", editable=False, auto_now=True)

class Grupos(models.Model):
    id_grupo = models.AutoField(verbose_name="id", primary_key=True, null=False)
    nombre   = models.CharField(verbose_name="Nombre", max_length=128, blank=True, null=False, default="")
    fh_alta  = models.DateTimeField(verbose_name="Fecha alta", editable=False, auto_now_add=True)
    fh_mod   = models.DateTimeField(verbose_name="Fecha modificación", editable=False, auto_now=True)

class Grupos_Usrs(models.Model):
    id_grupo = models.IntegerField(verbose_name="Id grupo", primary_key=True, null=False) #Grupos.id_grupo
    id_usr   = models.IntegerField(verbose_name="id usuario", primary_key=True, null=False) #Usuarios.id

class Permisos(models.Model):
    id_permi = models.AutoField(verbose_name="id", primary_key=True, null=False)
    nombre   = models.CharField(verbose_name="Nombre", max_length=128, blank=True, null=False, default="")
    fh_alta  = models.DateTimeField(verbose_name="Fecha alta", editable=False, auto_now_add=True)
    fh_mod   = models.DateTimeField(verbose_name="Fecha modificación", editable=False, auto_now=True)

class Permisos_Grps(models.Model):
    id_grupo = models.IntegerField(verbose_name="Id grupo", primary_key=True, null=False) #Grupos.id_grupo
    id_permi = models.IntegerField(verbose_name="Id permiso", primary_key=True, null=False) #Grupos.id_permi
    fh_alta  = models.DateTimeField(verbose_name="Fecha alta", editable=False, auto_now_add=True)
    fh_mod   = models.DateTimeField(verbose_name="Fecha modificación", editable=False, auto_now=True)

'''
#JABM(02/02/2025): Creo que no conviene tener permisos por usuario, si no que solo por grupos y los usuarios estan relacionados a los grupos
class Permisos_Usrs(models.Model):
    id_Usr[pk, fk]
    id_Permi[pk, fk]
    fh_alta  = models.DateTimeField(verbose_name="Fecha alta", editable=False, auto_now_add=True)
    fh_mod   = models.DateTimeField(verbose_name="Fecha modificación", editable=False, auto_now=True)
'''

