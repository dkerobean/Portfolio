from django.urls  import path 
from . import views 


urlpatterns = [
    path('home/', views.adminHome, name="admin-home"), 
    
    path('login/', views.adminLogin, name = "login"), 
    path('logout', views.userLogout, name="logout"),
    
    path('inbox/', views.adminInbox, name="admin-inbox"),
    path('inbox/<str:pk>/', views.inboxRead, name="inbox-read"),
    path('inbox/delete/<str:pk>/', views.deleteMessage, name="delete-message"),
    
    path('contact/create/', views.createContact, name="create-contact"),
    path('contact/view/', views.viewContact, name="view-contact"), 
    path('contact/update/<str:pk>/', views.updateContact, name="update-contact"), 
    path('contact/delete/<str:pk>/', views.deleteContact, name="delete-contact"),
    
    path('review/add/', views.createReview, name="create-review"), 
    path('review/all/', views.viewReview, name="view-reviews"), 
    path('review/update/<str:pk>/', views.updateReview, name="update-review"),
    path('review/delete/<str:pk>', views.deleteReview, name="delete-review"),

    path('project/all', views.createProject, name="create-project"), 
    path('project/update/<str:pk>/', views.updateProject, name="update-project"), 
    path('projects/all/', views.viewProjects, name="view-projects"), 
    path('project/delete/<str:pk>/', views.deleteProject, name="delete-project"),
    
    path('socials/add/', views.createSocial, name="create-social"), 
    path('socials/view/', views.viewSocial, name="view-social"),
    path('socials/update/<str:pk>/', views.updateSocial, name="update-social"),
    
]
