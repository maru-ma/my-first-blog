# Import path and views from blog app
from django.urls import path
from . import views

urlpatterns = [
    # Asociamos path raìz con la vista post_list
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
