from django.contrib import admin
from django.urls import path,include
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('music/',include('music.urls')),
    path('sadmin/',include('sadmin.urls'))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)