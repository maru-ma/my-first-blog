# Import path and views from blog app
from django.urls import path
from . import views

urlpatterns = [
    # Asociamos path raìz con la vista post_list
    path('', views.post_list, name='post_list')
]
