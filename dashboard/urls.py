from django.urls  import path 
from . import views 


urlpatterns = [
    path('home/', views.home, name="admin-home"), 
    path('login/', views.adminLogin, name = "login")
]
