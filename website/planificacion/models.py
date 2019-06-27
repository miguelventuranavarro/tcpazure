from django.db import models
from django.contrib.auth.models import User,Group,Permission
#from geocerca.models import *

# Create your models here.
class PlanificacionCargaBulto(models.Model):
    fecha_carga = models.DateTimeField()
    numero_carga = models.CharField(max_length=20)
    destino = models.IntegerField()
    local = models.CharField(max_length=45, blank=True, null=True)
    paradas = models.IntegerField(blank=True, null=True)
    numero_lpn = models.CharField(unique=True, max_length=25)
    peso = models.FloatField(blank=True, null=True)
    volumen = models.FloatField(blank=True, null=True)
    guia_remision = models.CharField(max_length=25, blank=True, null=True)
    fecha_llegada = models.DateTimeField(blank=True, null=True)
    region = models.CharField(max_length=25, blank=True, null=True)
    fecha_registro = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    #ruta_codigo = models.CharField(max_length=10, blank=True, null=True)
    ruta_codigo = models.ForeignKey('PlanificacionRuta', models.DO_NOTHING, db_column='ruta_codigo')
    transportista = models.CharField(max_length=45, blank=True, null=True)
    numero_placa = models.CharField(max_length=12, blank=True, null=True)
    #usuario_id = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_llegada_inicial = models.DateTimeField(blank=True, null=True)
    unidades = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'planificacion_carga_bulto'
        unique_together = (('id', 'numero_lpn'),)

class PrePlanificacionCargaBulto(models.Model):
    fecha_carga = models.DateTimeField()
    numero_carga = models.CharField(max_length=20)
    destino = models.IntegerField()
    local = models.CharField(max_length=45, blank=True, null=True)
    paradas = models.IntegerField(blank=True, null=True)
    numero_lpn = models.CharField(unique=True, max_length=25)
    peso = models.FloatField(blank=True, null=True)
    volumen = models.FloatField(blank=True, null=True)
    guia_remision = models.CharField(max_length=25, blank=True, null=True)
    fecha_llegada = models.DateTimeField(blank=True, null=True)
    region = models.CharField(max_length=25, blank=True, null=True)
    fecha_registro = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    ruta_codigo = models.ForeignKey('PlanificacionRuta', models.DO_NOTHING, db_column='ruta_codigo')
    transportista = models.CharField(max_length=45, blank=True, null=True)
    numero_placa = models.CharField(max_length=12, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_llegada_inicial = models.DateTimeField(blank=True, null=True)
    unidades = models.IntegerField(blank=True, null=True)


    class Meta:
        db_table = 'pre_planificacion_carga_bulto'

class PuntoGeocerca(models.Model):
    lpn = models.CharField(max_length=50)
    geo_code = models.CharField(max_length=50)
    us = models.IntegerField()
    id_control = models.IntegerField()
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = 'punto_geo'

class MarcacionesMatch(models.Model):
    lpn = models.CharField(max_length=50)
    id_marcacion = models.IntegerField()
    us = models.IntegerField()
    id_control = models.IntegerField()
    dentro = models.IntegerField()
    cnt_nombre = models.CharField(max_length=50)
    punto = models.CharField(max_length=50)
    fecha_marca = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'marcaciones_match'


class PlanificacionPermisos(models.Model):
    us = models.ForeignKey(User, models.DO_NOTHING, unique=True)
    carga_masiva = models.IntegerField()
    geocercas = models.IntegerField()
    consulta_registros = models.IntegerField()
    consulta_incidentes = models.IntegerField()
    registro_manual = models.IntegerField()
    pre_liquidacion = models.IntegerField()
    

    class Meta:
        db_table = 'planificacion_permisos'



class PlanificacionCargaMasiva(models.Model):
    nombre = models.CharField(max_length=20, blank=True, null=True)
    fecha_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'planificacion_carga_masiva'


class PlanificacionCargaPuntoControl(models.Model):
    numero_placa = models.CharField(max_length=12)
    numero_lpn = models.CharField(max_length=25)
    latitud = models.CharField(max_length=30, blank=True, null=True)
    longitud = models.CharField(max_length=30, blank=True, null=True)
    #empresa = models.IntegerField(blank=True, null=True)
    fecha_registro = models.DateTimeField()
    fecha_envio = models.DateTimeField()
    coordenadas = models.CharField(max_length=100, blank=True, null=True)
    coordenadas_poligon = models.CharField(max_length=100, blank=True, null=True)
    usuario = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'planificacion_carga_punto_control'

class PlanificacionPuntoControl(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    ruta_codigo = models.ForeignKey('PlanificacionRuta', models.DO_NOTHING, db_column='ruta_codigo')
    tipo_control = models.ForeignKey('PlanificacionTipoControl', models.DO_NOTHING)
    geocerca = models.ForeignKey('PlanificacionGeocerca', models.DO_NOTHING, blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'planificacion_punto_control'
    def __str__(self):
        return "%s" % (self.nombre)

    # def save(self, *args, **kwargs):
    #     super(PlanificacionPuntoControl, self).save()
    #     ruta = PlanificacionRuta.objects.get(codigo=self.ruta_codigo)
    #     puntos = ruta.numero_puntos + 1
    #     PlanificacionRuta.objects.filter(codigo=self.ruta_codigo).update(numero_puntos = puntos)
    

class PlanificacionDetalleGeocerca(models.Model):
    latitud = models.CharField(max_length=30, blank=True, null=True)
    longitud = models.CharField(max_length=30, blank=True, null=True)
    geocerca = models.ForeignKey('PlanificacionGeocerca', on_delete=models.CASCADE)

    class Meta:
        db_table = 'planificacion_detalle_geocerca'


class PlanificacionGeocerca(models.Model):
    codigo = models.CharField(max_length=45, blank=True, null=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    tipo_geocerca = models.ForeignKey('PlanificacionTipoGeocerca', models.DO_NOTHING)
    coordenadas = models.CharField(max_length=500, blank=True, null=True)
    coordenadas_poligon = models.CharField(max_length=500, blank=True, null=True)
    tarifa = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'planificacion_geocerca'
    def __str__(self):
        return "%s" % (self.nombre)


class PlanificacionIncidencia(models.Model):
    numero_placa = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=250)
    ruta = models.CharField(max_length=10)
    latitud = models.CharField(max_length=30, blank=True, null=True)
    longitud = models.CharField(max_length=30, blank=True, null=True)
    #empresa = models.IntegerField()
    fecha_registro = models.DateTimeField()
    fecha_envio = models.DateTimeField()
    coordenadas = models.CharField(max_length=100, blank=True, null=True)
    coordenadas_poligon = models.CharField(max_length=100, blank=True, null=True)
    usuario = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    primer_foto = models.FileField(upload_to='fotos/',blank=True, null=True)
    segunda_foto = models.FileField(upload_to='fotos/',blank=True, null=True)
    tercer_foto = models.FileField(upload_to='fotos/',blank=True, null=True)

    class Meta:
        db_table = 'planificacion_incidencia'


class PlanificacionRuta(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10)
    #numero_puntos = models.IntegerField()
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'planificacion_ruta'
    def __str__(self):
        return "%s" % (self.codigo)


class PlanificacionTipoControl(models.Model):
    nombre = models.CharField(max_length=25, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'planificacion_tipo_control'
    def __str__(self):
        return "%s" % (self.nombre)


class PlanificacionTipoGeocerca(models.Model):
    nombre = models.CharField(max_length=20)
    descripcions = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'planificacion_tipo_geocerca'
    def __str__(self):
        return "%s" % (self.nombre)

class TokenUsuarioDispositivo(models.Model):
    codigo_dispositivo = models.CharField(max_length=45, blank=True, null=True)
    usuario = models.IntegerField()
    estado = models.IntegerField()
    token = models.CharField(max_length=45, blank=True, null=True)
    fecha_registro = models.DateTimeField()

    class Meta:
        db_table = 'token_usuario_dispositivo'

class PlanificacionUsuarioRuta(models.Model):
    usuario = models.ForeignKey(User, models.DO_NOTHING)
    ruta_codigo = models.ForeignKey('PlanificacionRuta', models.DO_NOTHING, db_column='ruta_codigo')

    class Meta:
        db_table = 'planificacion_usuario_ruta'