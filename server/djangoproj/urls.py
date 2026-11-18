
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Website pages
    path('', include('dealers.web_urls')),

    # REST API
    path('api/', include('dealers.urls')),
]
