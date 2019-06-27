'''from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import View
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import render

from apps.home.forms.form import *

class index(SingleObjectMixin, FormView):
    form_class = MyForm
    initial = {'key': 'value'}
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})'''

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import View
'''from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import render

from apps.home.forms.form import *

from rest_framework import viewsets
from apps.home.serializers import UserSerializer, GroupSerializer

class index(SingleObjectMixin, FormView):
    form_class = MyForm
    initial = {'key': 'value'}
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer'''


from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from planificacion.models import *
from planificacion.punto_geo import PuntoGeo

from django.db import DatabaseError, transaction



@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("usuario")
    password = request.data.get("contrasena")
    group_name = request.data.get("empresa")
    codigo_dispositivo = request.data.get("codigo_dispositivo")

    if username is None or password is None or group_name is None:
        return Response({'error': 'Ingrese ussuario y contrasena'},
                        status=HTTP_200_OK)

    import hashlib
    token = hashlib.md5(str(codigo_dispositivo).encode('utf8')).hexdigest()

    import datetime
    now = datetime.datetime.now()

    try:
        user = authenticate(username=username, password=password)

        if not user:
            return Response({'error': 'Credencial invalida.'},
                        status=HTTP_200_OK)


        try:
            token_us = TokenUsuarioDispositivo.objects.get(token=token)

            if token_us.estado == 0:
                token_us.estado = 1
                token_us.save()
            
        except TokenUsuarioDispositivo.DoesNotExist:
            token_us = TokenUsuarioDispositivo.objects.create(usuario=user.id,token=token,estado=1,fecha_registro=now,codigo_dispositivo=codigo_dispositivo)
         
        return Response({'token': token_us.token},
                        status=HTTP_200_OK)   

    except User.DoesNotExist:
        return Response({'error': 'Credencial invalida.'},
                        status=HTTP_200_OK)

    '''user = authenticate(username=username, password=password)

    if not user:
        user_us.is_active=0
        user_us.save()

    try:
        group = Group.objects.get(name=group_name)
        group.user_set.filter(id=user_us.id)
    except Group.DoesNotExist:
        return Response({'error': 'Credencial invalida.'},
                        status=HTTP_400_BAD_REQUEST)

    if not user:
        return Response({'error': 'Credencial invalida.'},
                        status=HTTP_404_NOT_FOUND)
    #token, _ = Token.objects.get_or_create(user=user)

    token, _ = TokenUsuarioDispositivo.objects.get_or_create(user=user)

    return Response({'token': token.token},
                    status=HTTP_200_OK)'''

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def logout(request):
    message = ''
    success = False
    token_us = request.data.get("token")
    if token_us is None :
        return Response({'error': 'Ingrese token'},
                        status=HTTP_200_OK)

    try:
        token = TokenUsuarioDispositivo.objects.get(token=token_us)
        token.estado=0
        token.save()
        success = True
    except Exception as e:
        return Response({"message": "Token no existe.", "succes": success},
                        status=HTTP_200_OK)

    return Response({"message": message, "success": success}, status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def registro_scaner(request):

    message = ''
    success = True
    token = request.data.get("token")
    data = request.data.get("data")
    
    valid_tokens = valid_token(token)

    if not valid_tokens:
        return Response({'success': False, 'message': 'Inicie sesión.'},
                        status=HTTP_200_OK)

    #if numero_placa is None or numero_lpn is None or latitud is None or longitud is None or token is None:
    #    return Response({'error': 'Todos los campos son obligatorios.'},
    #                    status=HTTP_400_BAD_REQUEST)

    import datetime
    now = datetime.datetime.now()

    import json

    try:
        dt = json.loads(data)
    except Exception as e:
        data = {'success': False, 'message': 'Error en formato de objeto (data).'}
        return Response(data, status=HTTP_200_OK)
    marcaciones = []
    try:
        with transaction.atomic():
            i = 0
            while i < len(dt):
                coordenadas = '{"lat": '+dt[i].get('latitud')+', "lng": '+dt[i].get('longitud')+'}'
                coordenadas_poligon = '('+dt[i].get('latitud')+' '+dt[i].get('longitud')+')'
                pcpc = PlanificacionCargaPuntoControl.objects.create(numero_lpn=dt[i].get('numero_lpn'),
                    numero_placa=dt[i].get('numero_placa'),fecha_registro=dt[i].get('fecha_registro'),
                    latitud=dt[i].get('latitud'),longitud=dt[i].get('longitud'),
                    fecha_envio=now,coordenadas=coordenadas,coordenadas_poligon=coordenadas_poligon,usuario_id=valid_tokens.usuario)
                i = i + 1
                marcaciones.append(pcpc)
            message = str(i) + ' Registros insertados.'
            bultos = PlanificacionCargaBulto.objects.all()
            PuntoGeo.crearPuntoGeo(bultos,valid_tokens.usuario,marcaciones)
    except Exception as e:
        message = 'Error al insertar registros.'+str(e)
        success = False

    
    data = {'success': success, 'message': message}
    return Response(data, status=HTTP_200_OK)

    #{{"numero_placa":"abc123", "numero_lpn":"BAN123123123","latitud":"10.123123","longitud":"10.121212"},{"numero_placa":"abc123", "numero_lpn":"BAN1231231232","latitud":"10.123123","longitud":"10.121212"}}

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def registro_incidencia(request):
    message = ''
    success = True
    numero_placa = request.data.get("numero_placa")
    descripcion_incidente = request.data.get("descripcion_incidente")
    ruta = request.data.get("ruta")
    latitud = request.data.get("latitud")
    longitud = request.data.get("longitud")
    fecha_registro = request.data.get("fecha_registro")
    token = request.data.get("token")
    primer_foto = request.data.get("primer_foto")
    segunda_foto = request.data.get("segunda_foto")
    tercer_foto = request.data.get("tercer_foto")

    valid_tokens = valid_token(token)

    if not valid_tokens:
        return Response({'success': False, 'message': 'Inicie sesión.'},
                        status=HTTP_200_OK)

    if numero_placa is None or descripcion_incidente is None or ruta is None or fecha_registro is None or latitud is None or longitud is None:
        return Response({'error': 'Todos los campos son obligatorios.'},
                        status=HTTP_200_OK)

    import datetime
    now = datetime.datetime.now()

    try:
        coordenadas = '{"lat": '+latitud+', "lng": '+longitud+'}'

        try:
            getRuta = PlanificacionRuta.objects.get(codigo=ruta)
        except Exception as e:
            return Response({'error': 'La ruta no existe.'},
                        status=HTTP_200_OK)

        PlanificacionIncidencia.objects.create(numero_placa=numero_placa,descripcion=descripcion_incidente,ruta=ruta,fecha_registro=fecha_registro,latitud=latitud,longitud=longitud,fecha_envio=now,coordenadas=coordenadas,usuario_id=valid_tokens.usuario,primer_foto=primer_foto,segunda_foto=segunda_foto,tercer_foto=tercer_foto)
        message = 'Registro insertado.'
    except PlanificacionIncidencia.DoesNotExist:
        message = 'Error al insertar registro.'
        success = False

    data = {'succes': success, 'message': message}
    return Response(data, status=HTTP_200_OK)

def valid_token(token):
    try:
        token = TokenUsuarioDispositivo.objects.get(token=token,estado=1)
        return token
    except TokenUsuarioDispositivo.DoesNotExist:
        return False

