from django.urls import path
from . import views

urlpatterns = [
    path('',views.mostrar),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # path('post/new/', views.post_edit, name='post_edit'),
]
