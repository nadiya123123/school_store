from django.urls import path
from . import views


app_name='school_store'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('new_page/', views.new_page, name='new_page'),
    path('form/', views.form, name='form'),
    path('logout/', views.logout_view, name='logout'),



    path('ajax/load-course/', views.load_course, name='ajax_load_course'),
]