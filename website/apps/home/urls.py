from django.conf.urls import url

from django.contrib.auth import views as auth_views

from django.urls import include, path
from apps.home.views import home_index as views
from apps.home.views.home_index import *
from django.contrib.auth.decorators import login_required



#router = routers.DefaultRouter()
urlpatterns = [
    url(r'^$', login_required(views.import_data), name='index'),
    url(r'^eliminar_carga/', login_required(views.eliminar_carga), name='eliminar_carga'),
    url(r'^guardar_carga/', login_required(views.guardar_carga), name='guardar_carga'),

    url(r'^listar_geocercas/', login_required(views.listar_geocercas), name='listar_geocercas'),
    url(r'^crear_geocercas/', login_required(views.crear_geocercas), name='crear_geocercas'),
    url(r'^eliminar_geocercas/', login_required(views.eliminar_geocercas), name='eliminar_geocercas'),
    #(r'^article/new/$', views.edit, {}, 'article_new'),
    url(r'^edita_geocercas/(?P<id>\d+)/$', login_required(views.edita_geocercas), {}, 'edita_geocercas'),
    url(r'^editar_geocercas/', login_required(views.editar_geocercas), {}, 'editar_geocercas'),
    url(r'^puntos_control/', login_required(views.puntos_control), {}, 'puntos_control'),

    url(r'^consulta_registros/', login_required(views.consulta_registros), {}, 'consulta_registros'),
    url(r'^registro_manual/', login_required(views.registro_manual), {}, 'registro_manual'),
    url(r'^registro_manual_scaner/', login_required(views.registro_manual_scaner), {}, 'registro_manual_scaner'),
    url(r'^consulta_incidencias/', login_required(views.consulta_incidencias), {}, 'consulta_incidencias'),
    path('modal1/<slug:lpn>/<slug:cnt>', Upmodal1.as_view(), name='up_modal1'),
    url(r'^excel/', login_required(views.Excel), name='excel_r'),

    url(r'^export_consulta_registros/', login_required(views.export_consulta_registros), {}, 'export_consulta_registros'),
    
    #url(r'^edita_ruta/(?P<id>\d+)/$', views.edita_ruta, {}, 'edita_ruta'),
    #url(r'^$', upload.as_view(), name='index'),
    #url(r'^$', views.import_data, name='uplink'),
    #path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(template_name='home/login.html'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')), # new
]