from django.conf.urls import url
'''from ec_frontend.decorators import validateLogin,validateUbicacion,validateUser,validateBuy,validateBuySuscripcion
from ec_frontend.decorators import validateLogin
from ec_frontend.suscripcion import views as suscripcion_views
from views.checkout_web import *
from views.checkout_landing import CheckoutLandingView, CheckoutValidate'''
#from views.home_index import *

from django.urls import include, path
from rest_framework import routers
from apps.services.views import *

from django.contrib import admin
#from apps.services.views import login, sample_api


'''urlpatterns = [
    #url(r'^home/index/', index, name='index'),
    url(r'^$', index.as_view(), name='index'),
]'''

#router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #path('admin/', admin.site.urls),
    #url(r'^$', index.as_view(), name='index'),
    #path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/login', login),
    path('api/logout', logout),
    path('api/sampleapi', sample_api),
    path('api/registro-scaner', registro_scaner),
    path('api/registro-incidencia', registro_incidencia),
]