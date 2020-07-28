from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from api.views import BookViewSet
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()
router.register('books', BookViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

# this is for django to display static files so that django will diplay the file through admin page also
# we include static file form media_url, 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)