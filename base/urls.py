from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='home'),
    path('list/', views.listPerson, name='list'),
    path('person/', views.searchPerson, name='search'),
    path('view/<str:pk>', views.viewPerson, name='view'),
    path('edit/<str:pk>', views.editPerson, name='edit'),
    path('delete/<str:pk>', views.deletePerson, name='delete')

]
