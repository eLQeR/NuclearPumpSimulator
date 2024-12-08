from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pumps/', views.pump_list, name='pump_list'),
    path('pumps/<int:pk>/', views.pump_detail, name='pump_detail'),
    path('pumps/<int:pk>/control/', views.pump_control, name='pump_control'),
    path('pumps/create/', views.pump_create, name='pump_create'),
    path('pumps/<int:pk>/update/', views.pump_update, name='pump_update'),
    path('pumps/<int:pk>/delete/', views.pump_delete, name='pump_delete'),
]
