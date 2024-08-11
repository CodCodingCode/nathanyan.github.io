# myapp/urls.py
from django.urls import path
from .views import hello_world
from .views import contact
from .views import error_page

urlpatterns = [
    path('', hello_world, name='hello_world'),

]
