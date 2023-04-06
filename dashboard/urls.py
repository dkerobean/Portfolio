from django.urls  import path 
from . import views 


urlpatterns = [
    path('home/', views.adminHome, name="admin-home"), 
    path('login/', views.adminLogin, name = "login"), 
    
    path('inbox/', views.adminInbox, name="admin-inbox"),
    path('inbox/<str:pk>', views.inboxRead, name="inbox-read"),
    
    path('contact/create/', views.createContact, name="create-contact"),
    path('contact/view/', views.viewContact, name="view-contact"), 
    path('contact/update/<str:pk>', views.updateContact, name="update-contact"), 
    
    path('review/add', views.createReview, name="create-review"), 
    path('review/all', views.viewReview, name="view-reviews"), 
    path('review/update/<str:pk>', views.updateReview, name="update-review")
    
]
