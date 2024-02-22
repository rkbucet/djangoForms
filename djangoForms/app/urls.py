from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:id>', views.deleteData, name='delete'),
    path('<int:id>', views.updateData, name='update')
]