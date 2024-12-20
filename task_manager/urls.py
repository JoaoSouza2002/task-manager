from django.contrib import admin
from django.urls import path, include
from tasks.views import home
from django.http import HttpResponse
from tasks.views import TaskViewsSet
from rest_framework import DefaultRouter

router = DefaultRouter()
router.register(r"tasks", TaskViewsSet)

def test_view(request):
    return HttpResponse('Está funcionando!')

urlpatterns = [
    path('api/', include(router.urls)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
]

urlpatterns = [
    path('', test_view, name='test'),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home , name='home'),
]

