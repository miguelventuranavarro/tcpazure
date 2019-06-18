from planificacion.models import PuntoGeocerca, PlanificacionPuntoControl,PlanificacionGeocerca,PlanificacionDetalleGeocerca,PlanificacionCargaPuntoControl,MarcacionesMatch

class PuntoGeo():

    def crearPuntoGeo(lpns,user,marcadores):
        codigos = []
        for lpn in lpns:
            puntos_control = PlanificacionPuntoControl.objects.filter(ruta_codigo=lpn.ruta_codigo)

            for pc in puntos_control:
                lpnbd = lpn.numero_lpn
                geo = ''
                if pc.tipo_control_id == 2:
                    geo = str(lpn.destino)
                else:
                    geo = pc.geocerca.codigo

                codigos.append(PuntoGeocerca(lpn=lpnbd,geo_code=geo,us=user,id_control=pc.orden,nombre=pc.nombre))

        # codigos = PuntoGeocerca.objects.filter(user=user)
        # PuntoGeocerca.objects.filter(user=user).delete()

        #marcadores = PlanificacionCargaPuntoControl.objects.all()

        
        for mar in marcadores:
            x1 = float(mar.latitud)
            y1 = float(mar.longitud)
            for cod in codigos:
                if mar.numero_lpn == cod.lpn:
                    puntosPoly = PlanificacionDetalleGeocerca.objects.filter(geocerca=PlanificacionGeocerca.objects.get(codigo=cod.geo_code))
                    poly = []
                    for py in puntosPoly:
                        x = float(py.latitud)
                        y = float(py.longitud)
                        poly.append((x,y))

                    if PuntoGeo.point_inside_polygon(x1,y1,poly):
                        MarcacionesMatch.objects.create(lpn=mar.numero_lpn,id_marcacion=mar.id,us=user,id_control=cod.id_control, dentro = 1, cnt_nombre =cod.nombre, punto=mar.latitud+', '+mar.longitud,fecha_marca=mar.fecha_registro)
                    else:
                        MarcacionesMatch.objects.create(lpn=mar.numero_lpn,id_marcacion=mar.id,us=user,id_control=cod.id_control, dentro = 0,cnt_nombre =cod.nombre, punto=mar.latitud+', '+mar.longitud,fecha_marca=mar.fecha_registro)


    def point_inside_polygon(x,y,poly):

        n = len(poly)
        inside =False

        p1x,p1y = poly[0]
        for i in range(n+1):
            p2x,p2y = poly[i % n]
            if y > min(p1y,p2y):
                if y <= max(p1y,p2y):
                    if x <= max(p1x,p2x):
                        if p1y != p2y:
                            xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x,p1y = p2x,p2y

        return inside
                        




        

