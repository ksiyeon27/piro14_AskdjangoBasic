from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
import debug_toolbar
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("shop/", include("shop.urls")),
    path("blog/", include("blog.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path("__debug__/", include(debug_toolbar.urls)),
]
