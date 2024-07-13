from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path , include
from Appin import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Appin.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)