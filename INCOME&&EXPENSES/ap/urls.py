from django.contrib import admin
from django.urls import path
from .views import expenses,details,create,update,delete,custlogin,registeruser,home
from django.contrib.auth.views import LogoutView
urlpatterns = [
   path('',home,name='home'),

   path('login/',custlogin.as_view(),name='login'),
   path('logout/',LogoutView.as_view(next_page ='login'),name='logout'),
   path('registeruser',registeruser.as_view(),name='register'),


   path('expenses',expenses.as_view(),name='expenses'),
   path('details/<int:pk>/',details.as_view(),name='details'),
   path('create',create.as_view(),name='create'),
   path('update/<int:pk>/',update.as_view(),name='update'),
   path('delete/<int:pk>/',delete.as_view(),name='delete')

]
