from planificacion.models import PlanificacionPermisos

def permisos(request):
    perm = ''
    try:
        perm = PlanificacionPermisos.objects.get(us=request.user.id)
    except:
        print('debe solicitar permisos')            
    return {'permisos': perm}