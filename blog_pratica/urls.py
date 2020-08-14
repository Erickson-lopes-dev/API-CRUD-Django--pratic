from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from api_blog.views import PhrasesViewSets

router = SimpleRouter()
router.register('frases', PhrasesViewSets)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('site/', include('website.urls')),
    path('rest_auth/', include('rest_auth.urls')),
    path('rest_auth/registration/', include('rest_auth.registration.urls'))
]

