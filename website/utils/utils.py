from django.db.models import Count
from django.db.models import Max
from planificacion.models import (
    PlanificacionPuntoControl, MarcacionesMatch, PlanificacionGeocerca
)


def get_max_ruta_codigo_planificacion_punto_control(lista_ruta_codigo):
    """
    Devuelve la ruta con mas puntos de control
    :param list_ruta_codigo: lista de rutas de codigo, type list.
    :return:
    """
    val = 0
    pla = PlanificacionPuntoControl.objects.values(
        'ruta_codigo'
    ).filter(
        ruta_codigo__in=lista_ruta_codigo
    ).annotate(
        num_ruta_codigo=Count(
            'ruta_codigo'
        )
    ).order_by(
        '-ruta_codigo'
    ).first()

    if pla:
        val = pla.get('num_ruta_codigo')
    return val

def get_list_ruta_codigo(carga_bulto):
    """
    Devuelve una lista con rutas de codigo, unicas.
    :param carga_bulto: queryset de la tabla PlanificacionCargaBulto
    :return:
    """
    val = []
    val = list(
        carga_bulto.values_list(
            'ruta_codigo',
            flat=True
        )
    )
    val = list(set(val))
    return val

def get_dict_carga_bulto(carga_bulto):
    """
    Devuelve un diccionario de carga bulto
    :param carga_bulto: contiene elementos de la tabla
    PlanificacionCargaBulto. type: queryset
    :return: val, type dict
    """
    val = list(carga_bulto.values(
        'destino',
        'numero_carga',
        'ruta_codigo',
        'numero_lpn',
        'fecha_carga',
        'transportista',
    ))
    return val

def get_list_destino_carga_bulto(carga_bulto):
    """
    Devuelve una lista de 'destino' de la tabla PlanificacionCargaBulto
    :param carga_bulto: contiene elementos de la tabla
    PlanificacionCargaBulto. type: queryset
    :return: val, type list
    """
    val = carga_bulto.values_list(
        'destino'
    )
    return val

def get_planificacion_geocerca(data, codigo):
    """
    Devuelve un objeto PlanificacionGeocerca segun criterio de busqueda
    :param codigo:  type int
    :return: pg_ type dict
    """
    #planificacion_geocerca = list(PlanificacionGeocerca.objects.values().all())
    pg_ = [pg for pg in data if pg.get('codigo') == str(codigo)]
    pg_ = pg_[0] if pg_ else {}
    return pg_

def get_num_planificacion_punto_control(data, ruta_codigo):
    """
    Devuelve la cantidad de objetos PlanificacionPuntoControl segun criterio de busqueda
    :param ruta_codigo: type str
    :return: ppc_ type int
    """
    #planificacion_punto_control = list(PlanificacionPuntoControl.objects.values().all())
    ppc_ = len([ppc for ppc in data if ppc.get('ruta_codigo_id') == ruta_codigo])
    #print(ppc_)
    return ppc_

def get_carga_bulto_filtered(carga_bulto, numero_carga, destino):
    """
    Devuelve una lista de diccionarios de PlanificacionCargaBulto segun creiterios
    de busqueda
    :param carga_bulto:  type dict
    :param numero_carga: type str
    :param destino: type int
    :return:  list
    """
    cb = [cb for cb in carga_bulto if cb.get('numero_carga') == numero_carga and cb.get('destino') == destino]
    return cb

def get_list_lpn(carga_bulto):
    """
    Devueve una lista con los codigos lpn
    :param carga_bulto: queryset de la tabla PlanificacionCargaBulto
    :return:
    """
    val = []
    val = list(
        carga_bulto.values_list(
            'numero_lpn',
            flat=True
        )
    )
    return val

def get_list_marcaciones_match(list_lpn):
    """
    Devuelve una lista de marcacionesmatch filtrados por lpn
    :param list_lpn: lista de lpn, type list
    :return: list_marcaciones_match, type list
    """
    list_marcaciones_match = []
    for l in chunks(list_lpn, 2000):
        list_marcaciones_match += list(MarcacionesMatch.objects.filter(
                lpn__in=l
            ).values().all())

    return list_marcaciones_match

def get_match(list_marcaciones_match, list_lpn, id_control):
    """
    Devuelve el numero de marcaciones coincidentes
    :param list_lpn: lista de lpn, type list
    :param list_id_control: type list
    :return: count, type integer
    """
    count = len([lmm for lmm in list_marcaciones_match if lmm.get('lpn') in list_lpn and lmm.get('id_control') == id_control])
    # count = 0
    # for l in chunks(list_lpn, 2000):
    #     count += MarcacionesMatch.objects.filter(
    #         lpn__in=l,
    #         id_control__in=list_id_control
    #     ).count()
    #     #print('match', count, l)
    return count

def get_inside(list_marcaciones_match, list_lpn, id_control):
    """
    Devuelve el numero de marcaciones dentro de la geocerca
    :param list_lpn: lista de lpn, type list
    :param id_control: type int
    :return: count, type integer
    """
    count = len([lmm for lmm in list_marcaciones_match if lmm.get('lpn') in list_lpn and lmm.get('id_control') == id_control and lmm.get('dentro') == 1])
    # count = 0
    # for l in chunks(list_lpn, 2000):
    #     count += MarcacionesMatch.objects.filter(
    #         lpn__in=l,
    #         id_control__in=list_id_control,
    #         dentro=1
    #     ).count()
    #     #print('inside', count)
    return count

def get_outside(list_marcaciones_match, list_lpn, id_control):
    """
    Devuelve el numero de marcaciones fuera de la geocerca
    :param list_lpn: lista de lpn, type list
    :param id_control: type int
    :return: count, type integer
    """
    count = len([lmm for lmm in list_marcaciones_match if lmm.get('lpn') in list_lpn and lmm.get('id_control') == id_control and lmm.get('dentro') == 0])
    # count = 0
    # for l in chunks(list_lpn, 2000):
    #     count += MarcacionesMatch.objects.filter(
    #         lpn__in=l,
    #         id_control__in=list_id_control,
    #         dentro=0
    #     ).count()
    #     #print('outside', count)
    return count

def get_count_marcaciones(data, lpn, id_control, dentro):
    """
    D
    :param lpn:
    :param id_control:
    :param dentro:
    :return:
    """
    #marcaciones_match = list(MarcacionesMatch.objects.values().all())
    if id_control:
        mm = [mm for mm in data if mm.get('lpn') == lpn and mm.get('id_control') == id_control and mm.get('dentro') == dentro]
    else:
        mm = [mm for mm in data if mm.get('lpn') == lpn and mm.get('dentro') == dentro]
    return mm

def get_marcaciones_for_report(data, lpn, id_marcacion, dentro):
    """

    :param data:
    :param kwargs:
    :return:
    """
    mm = [mm for mm in data if mm.get('lpn') == lpn and mm.get('dentro') == dentro and mm.get('id_marcacion') == id_marcacion]
    return mm


def chunks(list_, interval):
    """
        Crea un generador con elementos de la longitud que se desea
    """
    for i in range(0, len(list_), interval):
        yield list_[i:i + interval]
