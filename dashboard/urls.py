from django.urls  import path 
from . import views 


urlpatterns = [
    path('home/', views.adminHome, name="admin-home"), 
    path('login/', views.adminLogin, name = "login"), 
    path('inbox/', views.adminInbox, name="admin-inbox"),
    path('inbox/<str:pk>', views.inboxRead, name="inbox-read"),
    
]
