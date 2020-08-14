from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from api_blog.views import PhrasesViewSets

router = routers.SimpleRouter()
router.register('phrases', PhrasesViewSets)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('site/', include('website.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
