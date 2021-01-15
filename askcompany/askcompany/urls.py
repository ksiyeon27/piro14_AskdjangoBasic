from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def mysum(request, x, y):
    result = x+y+100
    return HttpResponse('result = {}'.format(result))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mysum/<int:x>/<int:y>', mysum),
]
