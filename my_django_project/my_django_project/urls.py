from django.contrib import admin
from django.urls import path
from relationship_app.views import book_list  # Import your view

urlpatterns = [
    path("admin/", admin.site.urls),  # Admin panel
    path("", book_list, name="home"),  # Root URL ('/') mapped to book_list
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),  # Include relationship_app URLs
]
