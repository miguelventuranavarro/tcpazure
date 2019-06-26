from django.contrib import admin
from planificacion.models import *

# Register your models here.
class planificacionCargaBultoAdmin(admin.ModelAdmin):
	model = PlanificacionCargaBulto
	list_display = ['id','fecha_carga','numero_carga','destino','local','paradas','numero_lpn','peso','volumen','guia_remision','fecha_llegada','region','transportista','ruta_codigo']

class planificacionRutaAdmin(admin.ModelAdmin):
	model = PlanificacionRuta
	list_display = ['codigo']

class planificacionTipoControlAdmin(admin.ModelAdmin):
	model = PlanificacionTipoControl
	list_display = ['id','nombre']

class planificacionPuntoControlAdmin(admin.ModelAdmin):
	model = PlanificacionPuntoControl
	list_display = ['id','nombre','ruta_codigo','tipo_control','geocerca']

class planificacionGeocercaAdmin(admin.ModelAdmin):
	model = PlanificacionGeocerca
	list_display = ['id','codigo','nombre','direccion','tipo_geocerca','coordenadas_poligon']

class planificacionDetalleGeocercaAdmin(admin.ModelAdmin):
	model = PlanificacionDetalleGeocerca
	list_display = ['id']

class planificacionCargaPuntoControlAdmin(admin.ModelAdmin):
	model = PlanificacionCargaPuntoControl
	list_display = ['id','numero_placa','numero_lpn','latitud','longitud','fecha_registro','fecha_envio']

class planificacionTipoGeocercaAdmin(admin.ModelAdmin):
	model = PlanificacionTipoGeocerca
	list_display = ['id']

class planificacionCargaMasivaAdmin(admin.ModelAdmin):
	model = PlanificacionCargaMasiva
	list_display = ['id']

class planificacionIncidenciaAdmin(admin.ModelAdmin):
	model = PlanificacionIncidencia
	list_display = ['id','numero_placa','descripcion','ruta','latitud','longitud','fecha_registro','fecha_envio', 'foto']
	
class planificacionUsuarioRutaAdmin(admin.ModelAdmin):
	model = PlanificacionUsuarioRuta
	list_display = ['id','ruta_codigo','usuario']

'''class datosClienteAdmin(admin.ModelAdmin):
	model = DatosCliente
	list_display = ['id']

class datosProveedorAdmin(admin.ModelAdmin):
	model = DatosProveedor
	list_display = ['id']

class datosCargoAdmin(admin.ModelAdmin):
	model = DatosCargo
	list_display = ['id']

class datosCargoEmpleadoAdmin(admin.ModelAdmin):
	model = DatosCargoEmpleado
	list_display = ['id']'''

admin.site.register(PlanificacionCargaBulto, planificacionCargaBultoAdmin)
admin.site.register(PlanificacionRuta, planificacionRutaAdmin)
admin.site.register(PlanificacionTipoControl, planificacionTipoControlAdmin)
admin.site.register(PlanificacionPuntoControl, planificacionPuntoControlAdmin)
admin.site.register(PlanificacionGeocerca, planificacionGeocercaAdmin)
admin.site.register(PlanificacionDetalleGeocerca, planificacionDetalleGeocercaAdmin)
admin.site.register(PlanificacionCargaPuntoControl, planificacionCargaPuntoControlAdmin)
admin.site.register(PlanificacionTipoGeocerca, planificacionTipoGeocercaAdmin)
admin.site.register(PlanificacionCargaMasiva, planificacionCargaMasivaAdmin)
admin.site.register(PlanificacionIncidencia, planificacionIncidenciaAdmin)
admin.site.register(PlanificacionUsuarioRuta, planificacionUsuarioRutaAdmin)