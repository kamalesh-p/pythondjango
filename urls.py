"""
Definition of urls for DjangoWebProject2/mathematics.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.mhome, name='mhome'),
    path('topic/', views.mtopic, name='mtopic'),
    path('comment/', views.mcomment, name='mcomment'),
    path('problem/', views.mproblem, name='mproblem'),
    path('display/', views.mdisplay, name='mdisplay'),
    path('programming/', views.mprogramming, name='mprogramming'),
    path('', views.mgraphics, name='mgraphics'),
]

