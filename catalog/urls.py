from django.conf import settings
from django.contrib import admin
from django.template.context_processors import static
from django.urls import path, include

from catalog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('catalog/', include('catalog.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = )