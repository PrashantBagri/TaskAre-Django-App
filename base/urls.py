from django.urls import path
from . import views


urlpatterns = [
    path('', views.taskare, name='home'),
    path('task/<str:pk>', views.taskPage , name="task"),
    path('edit-task/<str:pk>', views.editTask , name="edit-task"),
    path('delete-task/<str:pk>', views.deleteTask , name="delete-task"),
    path('deletion/<str:pk>', views.deleteTask , name="deletion"),
    path('login/', views.loginPage , name="login"),
    path('logout/', views.logoutPage , name="logout"),
    path('Completed/<str:pk>', views.taskCompleted , name="Completed"),


    # path('register/', views.registerPage , name="register"),


    path('register/', views.registerPage , name="register"),



]
