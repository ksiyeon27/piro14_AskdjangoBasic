from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls')),
]


urlpatterns += [

    path('__debug__/', include(debug_toolbar.urls)),
]   