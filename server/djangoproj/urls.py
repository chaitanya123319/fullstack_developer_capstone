from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Course-standard API: /djangoapp/login, /logout, /get_cars, /get_dealers ...
    # Keep this ABOVE the '' include so a catch-all page route can't swallow it.
    path('djangoapp/', include('djangoapp.urls')),

    # Website pages
    path('', include('dealers.web_urls')),

    # REST API
    path('api/', include('dealers.urls')),
]
