"""
Definition of urls for DjangoWebProject2/DjangoWebProject2.
"""

from django.urls import path, include
from django.contrib import admin
urlpatterns = [
    path('',include('mathematics.urls')),
    path('admin/', admin.site.urls),
]

  